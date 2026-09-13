import {build} from 'esbuild';
import {mkdir,copyFile,writeFile} from 'node:fs/promises';
import {execFileSync} from 'node:child_process';
await mkdir('docs/app',{recursive:true});
await copyFile('v2/catalog-demo.json','docs/app/catalog.json');
await build({entryPoints:['v2/app.mjs'],bundle:true,minify:true,format:'esm',target:'es2022',outfile:'docs/app/app.js'});
for(const name of ['index.html','styles.css','sw.js'])await copyFile('v2/'+name,'docs/app/'+name);
await writeFile('docs/app/manifest.webmanifest',JSON.stringify({name:'Jardineando',short_name:'Jardineando',lang:'es',start_url:'./',scope:'./',display:'standalone',background_color:'#f7f7f2',theme_color:'#243c2c',icons:[{src:'../icon-192.png',sizes:'192x192',type:'image/png'},{src:'../icon-512.png',sizes:'512x512',type:'image/png'}]}));
console.log('Built docs/app/ — legacy app unchanged.');
