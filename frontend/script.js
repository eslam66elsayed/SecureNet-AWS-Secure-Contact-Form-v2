const form=document.getElementById('contactForm');
const button=document.getElementById('submitBtn');
const status=document.getElementById('status');
form.addEventListener('submit',async e=>{
  e.preventDefault(); button.disabled=true; status.textContent='Sending...';
  const payload={name:document.getElementById('name').value.trim(),email:document.getElementById('email').value.trim(),subject:document.getElementById('subject').value.trim(),message:document.getElementById('message').value.trim()};
  try{
    const r=await fetch('/api/contact',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify(payload)});
    const data=await r.json().catch(()=>({}));
    if(!r.ok) throw new Error(data.error||'Request failed');
    status.textContent=`Message sent successfully. Reference ID: ${data.id ?? 'created'}`; form.reset();
  }catch(err){status.textContent=err.message||'Something went wrong';}
  finally{button.disabled=false;}
});
