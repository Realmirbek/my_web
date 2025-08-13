function t(n,e){return{customHTMLBodyStart:`<!-- Google Tag Manager (noscript) -->
<noscript><iframe src="https://www.googletagmanager.com/ns.html?id=GTM-MPWDPWPL" height="0" width="0" style="display:none;visibility:hidden"></iframe></noscript>
<!-- End Google Tag Manager (noscript) -->`,customHTMLHeadEnd:`<script>
    !function(t,e){var o,n,p,r;e.__SV||(window.posthog=e,e._i=[],e.init=function(i,s,a){function g(t,e){var o=e.split(".");2==o.length&&(t=t[o[0]],e=o[1]),t[e]=function(){t.push([e].concat(Array.prototype.slice.call(arguments,0)))}}(p=t.createElement("script")).type="text/javascript",p.async=!0,p.src=s.api_host+"/static/array.js",(r=t.getElementsByTagName("script")[0]).parentNode.insertBefore(p,r);var u=e;for(void 0!==a?u=e[a]=[]:a="posthog",u.people=u.people||[],u.toString=function(t){var e="posthog";return"posthog"!==a&&(e+="."+a),t||(e+=" (stub)"),e},u.people.toString=function(){return u.toString(1)+".people (stub)"},o="capture identify alias people.set people.set_once set_config register register_once unregister opt_out_capturing has_opted_out_capturing opt_in_capturing reset isFeatureEnabled onFeatureFlags getFeatureFlag getFeatureFlagPayload reloadFeatureFlags group updateEarlyAccessFeatureEnrollment getEarlyAccessFeatures getActiveMatchingSurveys getSurveys onSessionId".split(" "),n=0;n<o.length;n++)g(u,o[n]);e._i.push([i,s,a])},e.__SV=1)}(document,window.posthog||[]);
    posthog.init('phc_kC80MWecgrgVgTinAZOHKWDVeIvYf8OtwNZ6gBTS4y0',{api_host:'https://app.posthog.com'})
<\/script>`,customHTMLHeadStart:`<!-- Google Tag Manager -->
<script>(function(w,d,s,l,i){w[l]=w[l]||[];w[l].push({'gtm.start':
new Date().getTime(),event:'gtm.js'});var f=d.getElementsByTagName(s)[0],
j=d.createElement(s),dl=l!='dataLayer'?'&l='+l:'';j.async=true;j.src=
'https://www.googletagmanager.com/gtm.js?id='+i+dl;f.parentNode.insertBefore(j,f);
})(window,document,'script','dataLayer','GTM-MPWDPWPL');<\/script>
<!-- End Google Tag Manager -->
<meta name="google-site-verification" content="6XVo4Mseofi78Qq8zwRgTawlI2_VA1S_jesOnbVMLIQ">
<!-- Universal Attribution Tracker \u0434\u043B\u044F nFactorial -->
<script>
(function() {
  // ============ \u041D\u0410\u0421\u0422\u0420\u041E\u0419\u041A\u0418 ============
  const CONFIG = {
    attribution_window_days: 30,  // \u0425\u0440\u0430\u043D\u0438\u043C 30 \u0434\u043D\u0435\u0439
    debug_mode: true,            // \u0412\u043A\u043B\u044E\u0447\u0438\u0442\u044C \u043B\u043E\u0433\u0438 \u0434\u043B\u044F \u043E\u0442\u043B\u0430\u0434\u043A\u0438
    storage_key: 'nfactorial_attribution'
  };
  
  // ============ \u041E\u0421\u041D\u041E\u0412\u041D\u041E\u0419 \u0422\u0420\u0415\u041A\u0415\u0420 ============
  window.AttributionTracker = {
    init: function() {
      console.log('\u{1F680} nFactorial Attribution Tracker starting...');
      this.captureAndSaveUTM();
      
      // \u0414\u0435\u043B\u0430\u0435\u043C \u0434\u043E\u0441\u0442\u0443\u043F\u043D\u044B\u043C \u0433\u043B\u043E\u0431\u0430\u043B\u044C\u043D\u043E
      window.getStoredAttribution = this.getAttribution.bind(this);
      
      // \u041E\u0442\u043B\u0430\u0434\u043A\u0430
      if (CONFIG.debug_mode) {
        console.log('\u2705 Attribution Tracker ready');
        console.log('\u{1F4CA} Current attribution:', this.getAttribution());
      }
    },
    
    captureAndSaveUTM: function() {
      const params = new URLSearchParams(window.location.search);
      let shouldSave = false;
      const attribution = {};
      
      // \u0421\u043E\u0431\u0438\u0440\u0430\u0435\u043C UTM \u043C\u0435\u0442\u043A\u0438
      const utmParams = ['utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content'];
      utmParams.forEach(param => {
        const value = params.get(param);
        if (value) {
          attribution[param] = value;
          shouldSave = true;
        }
      });
      
      // \u041F\u0440\u043E\u0432\u0435\u0440\u044F\u0435\u043C click ID \u043E\u0442 \u0440\u0435\u043A\u043B\u0430\u043C\u043D\u044B\u0445 \u0441\u0438\u0441\u0442\u0435\u043C
      if (params.get('fbclid')) {
        attribution.fbclid = params.get('fbclid');
        attribution.utm_source = attribution.utm_source || 'facebook';
        attribution.utm_medium = attribution.utm_medium || 'paid';
        shouldSave = true;
      }
      
      if (params.get('gclid')) {
        attribution.gclid = params.get('gclid');
        attribution.utm_source = attribution.utm_source || 'google';
        attribution.utm_medium = attribution.utm_medium || 'cpc';
        shouldSave = true;
      }
      
      if (params.get('yclid')) {
        attribution.yclid = params.get('yclid');
        attribution.utm_source = attribution.utm_source || 'yandex';
        attribution.utm_medium = attribution.utm_medium || 'cpc';
        shouldSave = true;
      }
      
      // \u0421\u043E\u0445\u0440\u0430\u043D\u044F\u0435\u043C \u0435\u0441\u043B\u0438 \u0435\u0441\u0442\u044C \u0434\u0430\u043D\u043D\u044B\u0435
      if (shouldSave) {
        attribution.timestamp = Date.now();
        attribution.landing_page = window.location.href;
        attribution.referrer = document.referrer;
        
        // \u0422\u0440\u043E\u0439\u043D\u043E\u0435 \u0441\u043E\u0445\u0440\u0430\u043D\u0435\u043D\u0438\u0435
        this.saveToStorage(attribution);
        
        // \u041E\u0442\u043F\u0440\u0430\u0432\u043B\u044F\u0435\u043C \u0432 PostHog
        if (typeof posthog !== 'undefined') {
          posthog.capture('utm_captured', attribution);
        }
        
        // \u041E\u0442\u043F\u0440\u0430\u0432\u043B\u044F\u0435\u043C \u0432 GTM
        if (typeof dataLayer !== 'undefined') {
          dataLayer.push({
            event: 'utm_captured',
            ...attribution
          });
        }
        
        console.log('\u{1F4BE} UTM saved:', attribution);
      }
    },
    
    saveToStorage: function(data) {
      const expiryTime = CONFIG.attribution_window_days * 24 * 60 * 60 * 1000;
      data.expires = Date.now() + expiryTime;
      
      // 1. LocalStorage - \u043E\u0441\u043D\u043E\u0432\u043D\u043E\u0435 \u0445\u0440\u0430\u043D\u0438\u043B\u0438\u0449\u0435
      try {
        localStorage.setItem(CONFIG.storage_key, JSON.stringify(data));
      } catch(e) {
        console.error('LocalStorage error:', e);
      }
      
      // 2. SessionStorage - \u0434\u043B\u044F \u0442\u0435\u043A\u0443\u0449\u0435\u0439 \u0441\u0435\u0441\u0441\u0438\u0438
      try {
        sessionStorage.setItem(CONFIG.storage_key + '_session', JSON.stringify(data));
      } catch(e) {
        console.error('SessionStorage error:', e);
      }
      
      // 3. Cookie - \u0440\u0435\u0437\u0435\u0440\u0432\u043D\u043E\u0435 \u0445\u0440\u0430\u043D\u0438\u043B\u0438\u0449\u0435
      try {
        document.cookie = \`\${CONFIG.storage_key}=\${encodeURIComponent(JSON.stringify(data))}; path=/; max-age=\${expiryTime/1000}\`;
      } catch(e) {
        console.error('Cookie error:', e);
      }
    },
    
    getAttribution: function() {
      // \u041F\u0440\u043E\u0431\u0443\u0435\u043C \u043F\u043E\u043B\u0443\u0447\u0438\u0442\u044C \u0438\u0437 \u0432\u0441\u0435\u0445 \u0438\u0441\u0442\u043E\u0447\u043D\u0438\u043A\u043E\u0432
      const sources = [
        () => JSON.parse(sessionStorage.getItem(CONFIG.storage_key + '_session') || 'null'),
        () => JSON.parse(localStorage.getItem(CONFIG.storage_key) || 'null'),
        () => {
          const match = document.cookie.match(new RegExp('(^| )' + CONFIG.storage_key + '=([^;]+)'));
          return match ? JSON.parse(decodeURIComponent(match[2])) : null;
        }
      ];
      
      for (let getSource of sources) {
        try {
          const data = getSource();
          if (data && (!data.expires || data.expires > Date.now())) {
            return data;
          }
        } catch(e) {
          continue;
        }
      }
      
      return {};
    }
  };
  
  // \u0417\u0430\u043F\u0443\u0441\u043A\u0430\u0435\u043C \u0441\u0440\u0430\u0437\u0443
  AttributionTracker.init();
})();
<\/script>`,description:"nFactorial School - \u043A\u0443\u0440\u0441\u044B \u043F\u043E \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0438\u0440\u043E\u0432\u0430\u043D\u0438\u044E \u0432 \u0410\u043B\u043C\u0430\u0442\u044B, \u041A\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043D \u0441 \u043D\u0443\u043B\u044F \u043E\u043D\u043B\u0430\u0439\u043D",favicon:"/static/site/framerusercontent.com/assets/lX5QcegD928dZZ7u51ccCsTJHU.png",robots:"max-image-preview:large",socialImage:"/static/site/framerusercontent.com/assets/f3ea7fXlzg1ZXyr6qEyFhhS4.jpg",title:"nFactorial School - \u043A\u0443\u0440\u0441\u044B \u043F\u043E \u043F\u0440\u043E\u0433\u0440\u0430\u043C\u043C\u0438\u0440\u043E\u0432\u0430\u043D\u0438\u044E \u0432 \u0410\u043B\u043C\u0430\u0442\u044B, \u041A\u0430\u0437\u0430\u0445\u0441\u0442\u0430\u043D \u0441 \u043D\u0443\u043B\u044F \u043E\u043D\u043B\u0430\u0439\u043D"}}export{t as a};
//# sourceMappingURL=chunk-K7CMTU4I.mjs.map
