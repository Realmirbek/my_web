import { s as p, t as i, w as a, x as c } from "./chunk-4FZPUS4R.mjs";
import { c as r } from "./chunk-A3IIQ6X3.mjs";

function y() {
  let [m, f] = i(false),       // валидность номера
      [u, d] = i(""),          // сообщение ошибки
      [l, h] = i(false),       // загрузка (отправка)
      b = p(null);             // реф на форму

  return c("div", {
    style: x,
    children: [
      c("form", {
        ref: b,
        onSubmit: async n => {
          n.preventDefault();
          if (!m || l) return;
          h(true);

          let o = new FormData(n.target);
          let e = o.get("number").replace(/\D/g, "");
          let t = e.startsWith("8") ? "+7" + e.substring(1) : "+" + e;

          // Формируем данные для отправки form-urlencoded
          const formData = new URLSearchParams();
          formData.append("name", o.get("name"));
          formData.append("phone", t);
          formData.append("message", "");  // или можно получить из формы, если есть поле

          // Можно добавить utm если нужно, например:
          const urlParams = new URLSearchParams(r.location.search);
          formData.append("utm_source", urlParams.get("utm_source") || "");
          formData.append("utm_medium", urlParams.get("utm_medium") || "");
          formData.append("utm_campaign", urlParams.get("utm_campaign") || "");
          formData.append("utm_term", urlParams.get("utm_term") || "");
          formData.append("utm_content", urlParams.get("utm_content") || "");

          try {
            await fetch("/send-contact", {
              method: "POST",
              headers: { "Content-Type": "application/x-www-form-urlencoded" },
              body: formData.toString()
            });
            r.location.href = "/";
          } catch (_) {
            console.error("Error submitting form:", _);
            d("Произошла ошибка при отправке формы");
            h(false);
          }
        },
        style: S,
        children: [
          a("input", {
            type: "text",
            name: "name",
            placeholder: "Имя",
            required: true,
            style: g
          }),
          a("input", {
            type: "tel",
            name: "number",
            placeholder: "+7 (___) ___-__-__",
            required: true,
            style: g,
            onChange: n => {
              let e = n.target.value.replace(/\D/g, "");
              e = e.substring(0, 11);
              let t = "";
              if (e.length > 0) {
                if (e[0] === "7" || e[0] === "8") {
                  t = "+7";
                  e = e.substring(1);
                } else if (e[0] === "9" || e.length > 1) {
                  t = "+7";
                }
                if (e.length > 0) t += " (" + e.substring(0, 3);
                if (e.length > 3) t += ") " + e.substring(3, 6);
                if (e.length > 6) t += "-" + e.substring(6, 8);
                if (e.length > 8) t += "-" + e.substring(8, 10);
              }
              n.target.value = t;
              let valid = e.length === 10 || (e.length === 11 && e[0] === "7");
              f(valid);
              d(valid ? "" : "Введите номер в формате +7 (XXX) XXX-XX-XX");
            }
          }),
          a("button", {
            type: "submit",
            disabled: !m || l,
            style: w,
            children: l ? "Отправка..." : "Получить консультацию"
          })
        ]
      }),
      u && a("p", { style: R, children: u })
    ]
  });
}

var x = {
  backgroundColor: "rgba(246, 246, 246, 0.2)",
  padding: "8px",
  borderRadius: "10px"
},
  S = {
    display: "flex",
    flexDirection: "row",
    gap: "10px"
  },
  g = {
    padding: "16px",
    border: "1px solid #EAE7E3",
    borderRadius: "10px",
    fontSize: "18px",
    color: "black"
  },
  w = {
    padding: "16px",
    border: "none",
    borderRadius: "10px",
    backgroundColor: "#E01424",
    color: "white",
    fontSize: "18px",
    cursor: "pointer"
  },
  R = {
    color: "red",
    fontWeight: "600",
    textAlign: "center"
  };

export { y as a };