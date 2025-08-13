import{m as y,t as r,w as e,x as l}from"./chunk-46A2A62J.mjs";import{c as n}from"./chunk-A3IIQ6X3.mjs";function S(){let[w,p]=r(!1),[i,E]=r(!1),[o,I]=r(!1),[T,_]=r(0);y(()=>{let c=()=>{let t=n.innerWidth<=768;I(t),t&&!i&&setTimeout(()=>s(),45e3)};c(),n.addEventListener("resize",c);let a=null,f=!1,k=()=>{i||s()},u=()=>{a&&clearTimeout(a),a=setTimeout(k,o?6e4:15e3)},m=()=>{u()},h=()=>{let t=n.innerHeight,M=document.documentElement.scrollHeight-t,v=n.scrollY/M*100;_(v),o&&v>70&&!i&&s(),m()},x=t=>{!o&&(t.clientY<=0||t.clientY>=n.innerHeight)&&(f=!0,s())},g=t=>{!o&&t.clientY<10&&!f&&s(),m()},b=()=>{m()},z=()=>{o&&!i&&s()},s=()=>{i||(p(!0),E(!0))};document.addEventListener("mouseleave",x),document.addEventListener("mousemove",g),document.addEventListener("touchstart",b),document.addEventListener("scroll",h),u();let d=null;return o&&(d=setTimeout(z,6e4)),()=>{n.removeEventListener("resize",c),document.removeEventListener("mouseleave",x),document.removeEventListener("mousemove",g),document.removeEventListener("touchstart",b),document.removeEventListener("scroll",h),a&&clearTimeout(a),d&&clearTimeout(d)}},[i,o,T]);let L=()=>{p(!1)},N=()=>{n.location.href="https://test.nfactorial.school?utm_source=website-popup&utm_medium=&utm_campaign="};return w?l("div",{className:"overlay",children:[l("div",{className:"modal",children:[e("button",{onClick:L,className:"close-button",children:"\xD7"}),l("h2",{className:"heading",children:["\u0427\u0435\u043B\u043E\u0432\u0435\u043A \u043C\u0435\u043D\u044F\u0435\u0442 \u0441\u0432\u043E\u044E",e("span",{className:"highlight",children:"\u043F\u0440\u043E\u0444\u0435\u0441\u0441\u0438\u044E 7 \u0440\u0430\u0437"})," \u0437\u0430 \u0436\u0438\u0437\u043D\u044C"]}),e("p",{className:"paragraph",children:"\u041F\u0440\u043E\u0439\u0434\u0438\u0442\u0435 \u0442\u0435\u0441\u0442 \u043F\u0440\u044F\u043C\u043E \u0441\u0435\u0439\u0447\u0430\u0441 \u0438 \u0443\u0437\u043D\u0430\u0439\u0442\u0435 \u043A\u0430\u043A\u0430\u044F \u043F\u0440\u043E\u0444\u0435\u0441\u0441\u0438\u044F \u0432\u0430\u043C \u043F\u043E\u0434\u043E\u0439\u0434\u0435\u0442 \u0431\u043E\u043B\u044C\u0448\u0435 \u0432\u0441\u0435\u0433\u043E"}),l("ul",{className:"benefits-list",children:[e("li",{className:"benefit-item",children:"\u2713 \u0411\u0435\u0441\u043F\u043B\u0430\u0442\u043D\u0430\u044F \u043A\u0430\u0440\u044C\u0435\u0440\u043D\u0430\u044F \u043A\u043E\u043D\u0441\u0443\u043B\u044C\u0442\u0430\u0446\u0438\u044F"}),e("li",{className:"benefit-item",children:"\u2713 \u041C\u043E\u043C\u0435\u043D\u0442\u0430\u043B\u044C\u043D\u044B\u0439 \u0440\u0435\u0437\u0443\u043B\u044C\u0442\u0430\u0442"}),e("li",{className:"benefit-item",children:"\u2713 \u041F\u0435\u0440\u0441\u043E\u043D\u0430\u043B\u044C\u043D\u044B\u0435 \u0440\u0435\u043A\u043E\u043C\u0435\u043D\u0434\u0430\u0446\u0438\u0438 \u043F\u043E \u0440\u0430\u0437\u0432\u0438\u0442\u0438\u044E"})]}),e("button",{onClick:N,className:"submit-button",children:"\u041F\u0440\u043E\u0439\u0442\u0438 \u0442\u0435\u0441\u0442 \u0431\u0435\u0441\u043F\u043B\u0430\u0442\u043D\u043E"}),e("p",{className:"guarantee",children:"5 \u043C\u0438\u043D\u0443\u0442 \u2022 100% \u043A\u043E\u043D\u0444\u0438\u0434\u0435\u043D\u0446\u0438\u0430\u043B\u044C\u043D\u043E \u2022 \u041C\u0433\u043D\u043E\u0432\u0435\u043D\u043D\u044B\u0439 \u0440\u0435\u0437\u0443\u043B\u044C\u0442\u0430\u0442"})]}),e("style",{jsx:!0,children:`
                .overlay {
                    position: fixed;
                    top: 0;
                    left: 0;
                    right: 0;
                    bottom: 0;
                    background-color: rgba(0, 0, 0, 0.5);
                    display: flex;
                    justify-content: center;
                    align-items: center;
                    z-index: 1000;
                    padding: 20px;
                }

                .modal {
                    background-color: white;
                    padding: 40px 30px;
                    border-radius: 12px;
                    width: 100%;
                    max-width: 500px;
                    position: relative;
                    animation: slideIn 0.3s ease-out;
                    box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
                }

                @keyframes slideIn {
                    from {
                        transform: translateY(20px);
                        opacity: 0;
                    }
                    to {
                        transform: translateY(0);
                        opacity: 1;
                    }
                }

                .close-button {
                    position: absolute;
                    right: 15px;
                    top: 15px;
                    border: none;
                    background: none;
                    font-size: 24px;
                    cursor: pointer;
                    color: #666;
                    padding: 5px;
                    width: 40px;
                    height: 40px;
                    display: flex;
                    align-items: center;
                    justify-content: center;
                    transition: color 0.3s ease;
                }

                .close-button:hover {
                    color: #333;
                }

                .heading {
                    margin-bottom: 40px;
                    color: #000;
                    font-size: clamp(24px, 5vw, 36px);
                    font-family: Inter, sans-serif;
                    font-weight: bold;
                    letter-spacing: -0.04em;
                    line-height: 1.2;
                    text-align: center;
                }

                .highlight {
                    color: #ff4757;
                    display: block;
                }

                .paragraph {
                    margin-bottom: 30px;
                    color: #333;
                    font-size: clamp(14px, 4vw, 16px);
                    font-family: Inter, sans-serif;
                    letter-spacing: -0.05em;
                    line-height: 1.4;
                    text-align: center;
                }

                .benefits-list {
                    list-style: none;
                    padding: 0;
                    margin: 30px 0;
                }

                .benefit-item {
                    font-size: clamp(16px, 4vw, 18px);
                    font-family: Inter, sans-serif;
                    color: #333;
                    margin-bottom: 12px;
                    display: flex;
                    align-items: center;
                    padding-left: 8px;
                }

                .submit-button {
                    width: 100%;
                    padding: clamp(15px, 4vw, 20px);
                    background-color: #ff4757;
                    color: white;
                    border: none;
                    border-radius: 8px;
                    cursor: pointer;
                    font-size: clamp(16px, 4vw, 20px);
                    font-weight: bold;
                    font-family: Inter, sans-serif;
                    transition: transform 0.2s ease, background-color 0.3s ease;
                    margin-bottom: 20px;
                }

                .submit-button:hover {
                    background-color: #ff6b81;
                    transform: scale(1.02);
                }

                .submit-button:active {
                    transform: scale(0.98);
                }

                .guarantee {
                    font-size: clamp(12px, 3.5vw, 14px);
                    color: #666;
                    text-align: center;
                    font-family: Inter, sans-serif;
                    margin: 0;
                }

                @media (max-width: 768px) {
                    .modal {
                        padding: 30px 20px;
                    }

                    .benefits-list {
                        margin: 20px 0;
                    }

                    .benefit-item {
                        margin-bottom: 10px;
                    }
                }

                @media (max-width: 480px) {
                    .overlay {
                        padding: 15px;
                    }

                    .heading {
                        margin-bottom: 24px;
                        font-size: 24px;
                    }
                    .paragraph{
                        font-size: 16px;
                    }
                }
            `})]}):null}export{S as a};
//# sourceMappingURL=chunk-V3RKV4BE.mjs.map
