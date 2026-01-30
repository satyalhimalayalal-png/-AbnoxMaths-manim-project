const DB_NAME = 'rpg_productivity';
const DB_VERSION = 1;
const STORE_NAME = 'heroData';
let db;
export const initDB = () => new Promise((resolve, reject) => {
    const request = indexedDB.open(DB_NAME, DB_VERSION);
    request.onupgradeneeded = (e) => {
        db = e.target.result;
        db.createObjectStore(STORE_NAME);
    };
    request.onsuccess = (e) => { db = e.target.result; resolve(); };
    request.onerror = (e) => reject(e);
});
export const saveData = async (id, data) => {
    return new Promise((resolve, reject) => {
        const tx = db.transaction(STORE_NAME, 'readwrite');
        tx.objectStore(STORE_NAME).put(data, id);
        tx.oncomplete = () => resolve();
        tx.onerror = e => reject(e);
    });
};
export const loadData = async (id) => new Promise((resolve, reject) => {
    const tx = db.transaction(STORE_NAME, 'readonly');
    const request = tx.objectStore(STORE_NAME).get(id);
    request.onsuccess = () => resolve(request.result);
    request.onerror = e => reject(e);
});