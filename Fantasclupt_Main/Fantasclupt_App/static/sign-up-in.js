let verifier=document.querySelectorAll("#otp_gen");
let otp_checker=document.querySelectorAll("#otp_checker");
let otp_box=document.getElementById("otp");
let otp_btn=document.getElementById("otp_checker");
let verify_btn=document.getElementById("verify");
let mail=document.getElementById("email");
let otp_gen=document.getElementById("otp_gen");

verifier.forEach(verification => {
    verification.addEventListener("click",()=>{
        otp_box.style.display="block";
        otp_btn.style.display="block";
        verify_btn.style.display="none";
        otp_box.setAttribute(required);
        otp_gen.setAttribute(href,"/otp-send/"+mail.value+"/");
    })
});