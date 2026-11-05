(function(){
const q = new URLSearchParams(location.search); const U = q.get("u") || "alice"; const RO = q.get("ro") === "1";
const UID = "u_" + U;
const GEN = "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Ccircle cx='12' cy='12' r='12' fill='%23999'/%3E%3C/svg%3E";
const NAMES = {alice: "김지현", bob: "박민수", carol: "이서연"}; const COLORS = {alice: "#D9480F", bob: "#1971C2", carol: "#2F9E44"};
const isObj = x => !!x && typeof x === "object" && !Array.isArray(x);
const merge = (a, b) => { const o = isObj(a) ? {...a} : {}; for(const k in b){ o[k] = isObj(b[k]) ? merge(o[k], b[k]) : b[k]; } return o; };
const KEY = "mockdb-store"; const bc = new BroadcastChannel("mockdb");
const load = () => { try { return JSON.parse(localStorage.getItem(KEY) || "{}"); } catch(e){ return {}; } };
let store = load(); const listeners = new Set();
const emit = () => listeners.forEach(l => l());
bc.onmessage = () => { store = load(); emit(); };
const save = () => { localStorage.setItem(KEY, JSON.stringify(store)); bc.postMessage(1); emit(); };
const wait = ms => new Promise(r => setTimeout(r, ms));
window.__writes = [];
function coll(path){
  const qq = {
    limit: () => qq,
    onSnapshot(next){ const fire = () => { const m = store[path] || {}; const docs = Object.keys(m).sort().map(id => ({id, exists: true, data: () => m[id], metadata: {fromCache: false, hasPendingWrites: false}})); next({docs, size: docs.length, empty: !docs.length, docChanges: () => [], metadata: {fromCache: false, hasPendingWrites: false}}); }; listeners.add(fire); setTimeout(fire, 30); return () => listeners.delete(fire); },
    get: async () => { const m = store[path] || {}; return {docs: Object.keys(m).map(id => ({id, exists: true, data: () => m[id]}))}; },
    doc: id => ({
      update: async d => { window.__writes.push(["update", path, id, JSON.parse(JSON.stringify(d))]); await wait(60); if(RO) throw {code: "invalid_argument", message: "denied"}; store = load(); if(!(store[path] && store[path][id])) throw {code: "invalid_argument", message: "missing"}; store[path][id] = merge(store[path][id], d); save(); },
      set: async d => { window.__writes.push(["set", path, id, JSON.parse(JSON.stringify(d))]); await wait(60); if(RO) throw {code: "invalid_argument", message: "denied"}; store = load(); (store[path] = store[path] || {})[id] = JSON.parse(JSON.stringify(d)); save(); },
      delete: async () => { store = load(); if(store[path]) delete store[path][id]; save(); }
    })
  };
  return qq;
}
const db = Object.freeze({collection: coll});
const user = Object.freeze({
  id: async () => UID, can: async () => !RO, isOwner: async () => U === "alice", canEdit: async () => U === "alice",
  profiles: async ids => { const o = {}; [].concat(ids).forEach(id => { const k = String(id).replace("u_", ""); o[id] = {id, name: NAMES[k] || "", avatarUrl: GEN, color: COLORS[k] || "#888", isMe: id === UID, email: null, guest: false}; }); return o; }
});
const peerId = Math.random().toString(36).slice(2); let myPres = {}; const peers = {}; const hs = new Set();
const rc = new BroadcastChannel("mockroom");
const list = () => Object.entries(peers).map(([p, v]) => ({peer: p, by: v.by, isMe: v.by === UID, sameTab: p === peerId, kind: "viewer", guest: false, presence: v.presence, updatedAt: v.updatedAt}));
const notify = () => { const ps = list(); hs.forEach(h => h({peers: ps, joined: [], left: [], updated: []})); };
peers[peerId] = {by: UID, presence: {}, updatedAt: Date.now()};
rc.onmessage = ev => { const m = ev.data; if(m.type === "pres"){ peers[m.peer] = {by: m.by, presence: m.presence, updatedAt: Date.now()}; notify(); if(m.hello) rc.postMessage({type: "pres", peer: peerId, by: UID, presence: myPres}); } else if(m.type === "bye"){ delete peers[m.peer]; notify(); } };
window.addEventListener("pagehide", () => rc.postMessage({type: "bye", peer: peerId}));
const room = Object.freeze({
  presence: async patch => { for(const k in patch){ if(patch[k] === null) delete myPres[k]; else myPres[k] = patch[k]; } peers[peerId] = {by: UID, presence: {...myPres}, updatedAt: Date.now()}; rc.postMessage({type: "pres", peer: peerId, by: UID, presence: {...myPres}}); notify(); },
  onPeers: h => { hs.add(h); setTimeout(notify, 10); return () => hs.delete(h); }
});
rc.postMessage({type: "pres", peer: peerId, by: UID, presence: {}, hello: true});
const downloads = Object.freeze({save: async ({filename, data}) => { window.__lastSave = {filename, data}; return {status: "saved"}; }});
window.claude = {use: async n => ({db, user, room, downloads})[n] || null};
})();
