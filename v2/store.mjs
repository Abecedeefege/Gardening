export function openStore(){return new Promise((resolve,reject)=>{const r=indexedDB.open('jardineando-v2',1);r.onupgradeneeded=()=>r.result.createObjectStore('accounts');r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);});}
export async function readState(key){const db=await openStore();return new Promise((resolve,reject)=>{const tx=db.transaction('accounts');const r=tx.objectStore('accounts').get(key);r.onsuccess=()=>resolve(r.result);r.onerror=()=>reject(r.error);tx.oncomplete=()=>db.close();});}
export async function writeState(key,value){const db=await openStore();return new Promise((resolve,reject)=>{const tx=db.transaction('accounts','readwrite');tx.objectStore('accounts').put(value,key);tx.oncomplete=()=>{db.close();resolve();};tx.onerror=()=>{db.close();reject(tx.error);};tx.onabort=()=>reject(tx.error);});}
export async function clearState(key){const db=await openStore();return new Promise((resolve,reject)=>{const tx=db.transaction('accounts','readwrite');tx.objectStore('accounts').delete(key);tx.oncomplete=()=>{db.close();resolve();};tx.onerror=()=>reject(tx.error);});}
export function mayEdit(state,userId){const g=state.gardens.find(x=>x.id===state.gardenId);return !!g&&(g.owner_id===userId||state.members.some(x=>x.garden_id===g.id&&x.user_id===userId&&x.role==='editor'));}
export function escapeHTML(value){return String(value??'').replace(/[&<>"']/g,c=>({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));}
export async function compressPhoto(file){
 if(!/^image\/(jpeg|png|webp)$/.test(file.type))throw new Error('Usá una foto JPG, PNG o WebP.');
 if(file.size>20*1024*1024)throw new Error('La foto debe pesar menos de 20 MB.');
 const source=await createImageBitmap(file);const ratio=Math.min(1,1280/Math.max(source.width,source.height));
 const canvas=document.createElement('canvas');canvas.width=Math.round(source.width*ratio);canvas.height=Math.round(source.height*ratio);
 canvas.getContext('2d').drawImage(source,0,0,canvas.width,canvas.height);source.close();
 const blob=await new Promise(r=>canvas.toBlob(r,'image/jpeg',0.78));
 if(!blob||blob.size>2097152)throw new Error('No pudimos reducir la foto. Probá otra.');return blob;
}
