<template>
  <div class="cross-platform-result-slide w-full my-auto flex flex-col justify-center h-full overflow-hidden">
    <!-- Clean Minimalist Header with Breakdown Button -->
    <div class="flex justify-between items-center mb-1.5">
      <h2 class="text-xl font-black tracking-tight text-white m-0 text-left">
        {{ currentLang === 'zh' ? '成果展示：' : 'The Result:' }}
        <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-blue-400">
          {{ currentLang === 'zh' ? '原生與 HTML 混合架構 📱🌐' : 'Native + HTML hybrid 📱🌐' }}
        </span>
      </h2>

      <!-- Toggle Architecture Callouts Button -->
      <button
        @click="showBreakdown = !showBreakdown"
        :class="[
          'px-2.5 py-1 rounded-lg border font-mono text-xs font-bold transition-all flex items-center gap-1.5 shadow-md cursor-pointer',
          showBreakdown
            ? 'bg-red-950/90 border-red-500 text-red-300 ring-1 ring-red-500/50 scale-105'
            : 'bg-slate-900 border-slate-700 text-slate-300 hover:text-white',
        ]"
      >
        <span>
          <template v-if="showBreakdown">
            {{ currentLang === 'zh' ? '❌ 重設預覽' : '❌ Reset Screenshots' }}
          </template>
          <template v-else>
            {{ currentLang === 'zh' ? '🎯 高亮 Native 與 HTML 區域' : '🎯 Highlight Native vs HTML' }}
          </template>
        </span>
      </button>
    </div>

    <!-- 3 Column Showcase Grid -->
    <div class="grid grid-cols-3 gap-3 items-stretch text-left flex-1 min-h-0">
      <!-- COLUMN 1: WEB BROWSER -->
      <div
        class="bg-slate-900/90 border border-red-500/30 rounded-xl p-2 shadow-lg flex flex-col justify-between overflow-hidden relative"
      >
        <div
          class="font-bold text-xs text-white border-b border-slate-800 pb-1 mb-1.5 flex items-center justify-between"
        >
          <span>🌐 Web Browser</span>
        </div>

        <div
          class="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-1 shadow-inner flex items-center justify-center overflow-hidden min-h-[290px] relative"
        >
          <img
            v-if="hasWebImage"
            :src="webImgSrc"
            alt="Web Browser Result"
            class="w-full h-full object-contain rounded"
          />
          <div v-else class="p-2 text-center space-y-0.5">
            <span class="text-xl">🌐</span>
            <div class="text-[10px] font-mono text-red-300 font-bold">Web Screenshot</div>
            <div class="text-[8px] text-slate-500 font-mono">result_web.jpg</div>
          </div>

          <!-- Red Outline Overlay for Web Browser -->
          <div
            v-if="showBreakdown"
            class="absolute inset-1 border-2 border-red-500 rounded pointer-events-none flex items-start justify-center p-1 animate-fade-in"
          >
            <span
              class="bg-red-600 text-white font-mono text-[9px] font-bold px-1.5 py-0.5 rounded shadow-lg uppercase tracking-wider"
            >
              100% Rails ERB HTML
            </span>
          </div>
        </div>
      </div>

      <!-- COLUMN 2: IOS NATIVE APP -->
      <div
        class="bg-slate-900/90 border border-blue-500/30 rounded-xl p-2 shadow-lg flex flex-col justify-between overflow-hidden relative"
      >
        <div
          class="font-bold text-xs text-white border-b border-slate-800 pb-1 mb-1.5 flex items-center justify-between"
        >
          <span>🍏 Native iOS</span>
        </div>

        <div
          class="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-1 shadow-inner flex items-center justify-center overflow-hidden min-h-[290px] relative"
        >
          <img
            v-if="hasIosImage"
            :src="iosImgSrc"
            alt="iOS App Result"
            class="w-full h-full object-contain rounded"
          />
          <div v-else class="p-2 text-center space-y-0.5">
            <span class="text-xl">🍏</span>
            <div class="text-[10px] font-mono text-blue-300 font-bold">iOS Screenshot</div>
            <div class="text-[8px] text-slate-500 font-mono">result_ios.jpg</div>
          </div>

          <!-- Red Outline Overlays for iOS -->
          <div
            v-if="showBreakdown"
            class="absolute inset-1 flex flex-col justify-between pointer-events-none animate-fade-in space-y-1"
          >
            <!-- Native Top Navbar Red Outline -->
            <div
              class="border-2 border-red-500 rounded h-[14%] flex items-center justify-center relative bg-red-950/20"
            >
              <span
                class="bg-red-600 text-white font-mono text-[8.5px] font-bold px-1 rounded shadow"
              >
                NATIVE TOP NAVBAR
              </span>
            </div>

            <!-- Central HTML Viewport Green/Red Outline -->
            <div
              class="border-2 border-emerald-400 rounded flex-1 flex items-center justify-center relative bg-emerald-950/20 my-0.5"
            >
              <span
                class="bg-emerald-600 text-white font-mono text-[9px] font-bold px-1.5 py-0.5 rounded shadow"
              >
                ⚡ RAILS HTML BODY
              </span>
            </div>

            <!-- Native Bottom Tabbar Red Outline -->
            <div
              class="border-2 border-red-500 rounded h-[14%] flex items-center justify-center relative bg-red-950/20"
            >
              <span
                class="bg-red-600 text-white font-mono text-[8.5px] font-bold px-1 rounded shadow"
              >
                NATIVE TAB BAR
              </span>
            </div>
          </div>
        </div>
      </div>

      <!-- COLUMN 3: ANDROID NATIVE APP -->
      <div
        class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-2 shadow-lg flex flex-col justify-between overflow-hidden relative"
      >
        <div
          class="font-bold text-xs text-white border-b border-slate-800 pb-1 mb-1.5 flex items-center justify-between"
        >
          <span>🤖 Native Android</span>
        </div>

        <div
          class="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-1 shadow-inner flex items-center justify-center overflow-hidden min-h-[290px] relative"
        >
          <img
            v-if="hasAndroidImage"
            :src="androidImgSrc"
            alt="Android App Result"
            class="w-full h-full object-contain rounded"
          />
          <div v-else class="p-2 text-center space-y-0.5">
            <span class="text-xl">🤖</span>
            <div class="text-[10px] font-mono text-emerald-300 font-bold">Android Screenshot</div>
            <div class="text-[8px] text-slate-500 font-mono">result_android.jpg</div>
          </div>

          <!-- Red Outline Overlays for Android -->
          <div
            v-if="showBreakdown"
            class="absolute inset-1 flex flex-col justify-between pointer-events-none animate-fade-in space-y-1"
          >
            <!-- Native Top Toolbar Red Outline -->
            <div
              class="border-2 border-red-500 rounded h-[14%] flex items-center justify-center relative bg-red-950/20"
            >
              <span
                class="bg-red-600 text-white font-mono text-[8.5px] font-bold px-1 rounded shadow"
              >
                NATIVE TOP TOOLBAR
              </span>
            </div>

            <!-- Central HTML Viewport Green Outline -->
            <div
              class="border-2 border-emerald-400 rounded flex-1 flex items-center justify-center relative bg-emerald-950/20 my-0.5"
            >
              <span
                class="bg-emerald-600 text-white font-mono text-[9px] font-bold px-1.5 py-0.5 rounded shadow"
              >
                ⚡ RAILS HTML BODY
              </span>
            </div>

            <!-- Native Bottom Nav Red Outline -->
            <div
              class="border-2 border-red-500 rounded h-[14%] flex items-center justify-center relative bg-red-950/20"
            >
              <span
                class="bg-red-600 text-white font-mono text-[8.5px] font-bold px-1 rounded shadow"
              >
                NATIVE BOTTOM NAV
              </span>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from "vue";
import { currentLang } from '../composables/useLang'

const showBreakdown = ref(false);

const webImgSrc = ref("/result_web.jpg");
const iosImgSrc = ref("/result_ios.jpg");
const androidImgSrc = ref("/result_android.jpg");

const hasWebImage = ref(false);
const hasIosImage = ref(false);
const hasAndroidImage = ref(false);

const checkImage = (url, refVar) => {
  const img = new Image();
  img.onload = () => {
    refVar.value = true;
  };
  img.onerror = () => {
    refVar.value = false;
  };
  img.src = url;
};

onMounted(() => {
  checkImage(webImgSrc.value, hasWebImage);
  checkImage(iosImgSrc.value, hasIosImage);
  checkImage(androidImgSrc.value, hasAndroidImage);
});
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: scale(0.98);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

.animate-fade-in {
  animation: fadeIn 0.2s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>
