// ゲーム側の受け口（index.html に1度だけ入れる）
function mdlMesh(m){const g=new THREE.Group();const f=s=>{const b=atob(s),u=new Uint8Array(b.length);for(let i=0;i<b.length;i++)u[i]=b.charCodeAt(i);return new Float32Array(u.buffer)};
 for(const p of m.parts){const ge=new THREE.BufferGeometry();ge.setAttribute('position',new THREE.BufferAttribute(f(p.p),3));ge.setAttribute('normal',new THREE.BufferAttribute(f(p.n),3));
  const me=new THREE.Mesh(ge,new THREE.MeshStandardMaterial({color:p.c,roughness:.7}));me.castShadow=me.receiveShadow=true;g.add(me)}return g}
