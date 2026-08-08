import os

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

# 1. HotwireInteractionSlide.vue
hotwire_interaction = '''<template>
  <div class="hotwire-interaction-slide w-full my-auto flex flex-col justify-center">
    <!-- Title Header -->
    <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left">
      {{ currentLang === 'zh' ? 'Hotwire Native 的互動運作機制 🔄' : 'How the Interaction Works 🔄' }}
    </h2>

    <!-- Layout Grid -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-stretch">
      <!-- Left Column: 3 Step Cards -->
      <div class="md:col-span-5 space-y-2.5 text-left flex flex-col justify-between">
        <div 
          @click="activeStep = 1"
          :class="[
            'p-3.5 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 1 
              ? 'bg-slate-900 border-amber-500/60 shadow-lg ring-1 ring-amber-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-80 hover:opacity-100'
          ]">
          <div class="flex items-start gap-3">
            <div :class="['w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm shrink-0', activeStep === 1 ? 'bg-amber-500/20 text-amber-400 border border-amber-500/40' : 'bg-slate-800 text-slate-400']">
              1
            </div>
            <div class="flex-1">
              <h4 class="text-xs font-bold text-white mb-1">{{ currentLang === 'zh' ? '1. 使用者點擊連結' : '1. User Taps a Link' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0">
                {{ currentLang === 'zh' ? '點擊卡片時，攔截標準瀏覽器重新整理，交由 Hotwire Native 接管。' : 'In LitLoop, tapping a book card interrupts default web reload and hands navigation to Hotwire Native.' }}
              </p>
            </div>
          </div>
        </div>

        <div 
          @click="activeStep = 2"
          :class="[
            'p-3.5 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 2 
              ? 'bg-slate-900 border-blue-500/60 shadow-lg ring-1 ring-blue-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-80 hover:opacity-100'
          ]">
          <div class="flex items-start gap-3">
            <div :class="['w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm shrink-0', activeStep === 2 ? 'bg-blue-500/20 text-blue-400 border border-blue-500/40' : 'bg-slate-800 text-slate-400']">
              2
            </div>
            <div class="flex-1">
              <h4 class="text-xs font-bold text-white mb-1">{{ currentLang === 'zh' ? '2. 原生轉場優先推入' : '2. Native Nav First' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0">
                {{ currentLang === 'zh' ? 'iOS 或 Android 立刻推入一個流暢的原生 ViewController 畫面。' : 'The iOS or Android app pushes a new native screen with smooth native transitions instantly.' }}
              </p>
            </div>
          </div>
        </div>

        <div 
          @click="activeStep = 3"
          :class="[
            'p-3.5 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 3 
              ? 'bg-slate-900 border-emerald-500/60 shadow-lg ring-1 ring-emerald-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-80 hover:opacity-100'
          ]">
          <div class="flex items-start gap-3">
            <div :class="['w-8 h-8 rounded-lg flex items-center justify-center font-bold text-sm shrink-0', activeStep === 3 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' : 'bg-slate-800 text-slate-400']">
              3
            </div>
            <div class="flex-1">
              <h4 class="text-xs font-bold text-white mb-1">{{ currentLang === 'zh' ? '3. 伺服器渲染 HTML' : '3. Render HTML' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0">
                {{ currentLang === 'zh' ? 'Rails 伺服器回傳 HTML，在原生畫面中展現 100% 網頁速度與原生流暢感。' : 'Rails server returns server-rendered HTML inside the native container.' }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Visual Diagram -->
      <div class="md:col-span-7 bg-slate-950 border border-slate-800 rounded-xl p-4 flex flex-col justify-between">
        <div class="text-xs font-mono text-slate-400 mb-2">
          {{ currentLang === 'zh' ? '互動流程示範' : 'Interaction Flow Visualization' }}
        </div>
        <div class="p-3 bg-slate-900 border border-slate-800 rounded-lg text-xs text-slate-200">
          <template v-if="activeStep === 1">
            ⚡ {{ currentLang === 'zh' ? '步驟 1：Web 點擊事件由 Hotwire Native 攔截' : 'Step 1: Web click intercepted by Hotwire Native' }}
          </template>
          <template v-if="activeStep === 2">
            🍏 {{ currentLang === 'zh' ? '步驟 2：原生視窗立刻滑出轉場動畫' : 'Step 2: Native push transition animating immediately' }}
          </template>
          <template v-if="activeStep === 3">
            💎 {{ currentLang === 'zh' ? '步驟 3：Rails 回傳 HTML 渲染至原生容器' : 'Step 3: Rails HTML view rendered inside native WebView' }}
          </template>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { currentLang } from '../composables/useLang'

const activeStep = ref(1)
</script>
'''

with open(f"{components_dir}/HotwireInteractionSlide.vue", "w") as f:
    f.write(hotwire_interaction)

# 2. WrapUpSlide.vue
wrap_up = '''<template>
  <div class="flex flex-col items-center justify-center h-auto my-auto px-4 text-center relative z-10 py-2">
    <div class="flex items-center gap-2 mb-2">
      <span class="rails-badge">💎 {{ currentLang === 'zh' ? '總結' : 'Wrap Up' }}</span>
      <span class="px-3 py-1 rounded-full text-xs font-mono font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/40 animate-pulse">
        ● Open for Senior / Staff / Lead Roles & Consulting
      </span>
    </div>

    <h1 class="text-4xl font-black mb-2">
      <template v-if="currentLang === 'zh'">
        極速開發。輕鬆維護。<br />
        <span class="text-red-500">
          使用 Rails 輕鬆發佈 Mobile App。
        </span>
      </template>
      <template v-else>
        Build Faster. Maintain Less. <br />
        <span class="text-red-500">
          Ship Mobile Apps with Rails.
        </span>
      </template>
    </h1>

    <p class="text-slate-300 text-xs max-w-xl mx-auto mb-4">
      {{ currentLang === 'zh'
        ? '單體架構。90%+ 程式碼重用率。Mobile 功能交付速度提升 80%！'
        : 'Single Majestic Monolith. 90%+ Code Reuse. 80% Faster Mobile Feature Delivery.' }}
    </p>

    <!-- Speaker Card -->
    <div class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-5 max-w-2xl w-full shadow-2xl backdrop-blur-md text-left">
      <div class="grid grid-cols-1 md:grid-cols-3 gap-4 items-center">
        <div class="md:col-span-2 space-y-2">
          <div class="flex items-center gap-3">
            <div class="w-12 h-12 rounded-xl bg-gradient-to-tr from-red-600 to-amber-500 p-0.5 shadow shrink-0 overflow-hidden">
              <img src="/nebiyu.png" alt="Nebiyu Elias Talefe" class="w-full h-full object-cover object-top rounded-[10px]" />
            </div>
            <div>
              <h3 class="text-base font-black text-white m-0 flex items-center gap-2 flex-wrap">
                Neba 🇪🇹
                <span class="text-[9px] bg-red-950 text-red-300 px-1.5 py-0.5 rounded border border-red-800 font-mono">Speaker</span>
                <span class="text-[9px] bg-cyan-950 text-cyan-300 px-1.5 py-0.5 rounded border border-cyan-800 font-mono">I use omarchy btw 🐧</span>
              </h3>
              <p class="text-xs text-red-400 font-semibold m-0 mt-0.5">
                Full-Stack Engineer (7+ Years Exp) • 🇪🇹 Ethiopia • ASUS • 508.dev
              </p>
            </div>
          </div>

          <ul class="text-xs text-slate-300 space-y-1 list-disc pl-4 leading-relaxed">
            <li>{{ currentLang === 'zh' ? '7+ 年全棧開發經驗 (來自埃塞俄比亞 🇪🇹，在台居留 3 年)' : 'Full-stack engineer with 7+ years exp (from Ethiopia, living in Taiwan for 3 years)' }}</li>
            <li>{{ currentLang === 'zh' ? '目前任職於 ASUS，且為 508.dev 工程合作社成員' : 'Currently working at ASUS and member of software engineer co-op 508.dev' }}</li>
            <li>{{ currentLang === 'zh' ? '已成功上架多款 Hotwire Native iOS/Android App' : 'Shipped Hotwire Native apps on iOS/Android' }}</li>
            <li>{{ currentLang === 'zh' ? '開源 Rails & React Native 起手式專案創作者' : 'Creator of open-source Rails & React Native starter template' }}</li>
          </ul>

          <div class="p-2 bg-emerald-950/60 border border-emerald-500/30 rounded-lg text-[11px] text-emerald-200 flex items-center justify-between gap-2">
            <span>💼 <strong>Hire Me:</strong> Senior/Staff Full-Stack & Mobile Roles</span>
            <a href="mailto:nebiyu@508.dev" class="px-2 py-0.5 bg-emerald-600 hover:bg-emerald-500 text-white font-mono font-bold rounded text-[10px] transition">
              ✉️ nebiyu@508.dev
            </a>
          </div>
        </div>

        <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-center flex flex-col items-center justify-center space-y-2">
          <div class="w-24 h-24 bg-white p-1.5 rounded-lg shadow-md flex items-center justify-center">
            <svg class="w-full h-full text-slate-950" viewBox="0 0 33 33" shape-rendering="crispEdges">
              <path fill="#ffffff" d="M0 0h33v33H0z"/>
              <path stroke="#000000" d="M4 4.5h7m6 0h1m4 0h7M4 5.5h1m5 0h1m5 0h4m2 0h1m5 0h1M4 6.5h1m1 0h3m1 0h1m1 0h1m1 0h1m3 0h3m1 0h1m1 0h3m1 0h1M4 7.5h1m1 0h3m1 0h1m1 0h1m4 0h1m1 0h2m1 0h1m1 0h3m1 0h1M4 8.5h1m1 0h3m1 0h1m1 0h5m3 0h1m1 0h1m1 0h3m1 0h1M4 9.5h1m5 0h1m1 0h2m3 0h1m1 0h2m1 0h1m5 0h1M4 10.5h7m1 0h1m1 0h1m1 0h1m1 0h1m1 0h1m1 0h7M12 11.5h1m2 0h1m2 0h3M4 12.5h1m1 0h5m2 0h2m2 0h3m2 0h5M5 13.5h1m1 0h1m1 0h1m2 0h1m3 0h1m1 0h1m1 0h1m2 0h1m3 0h1M5 14.5h4m1 0h1m1 0h1m5 0h2m1 0h2m1 0h2m1 0h2M4 15.5h3m2 0h1m1 0h1m8 0h5m3 0h1M4 16.5h1m1 0h2m1 0h6m2 0h2m2 0h2m1 0h1m1 0h3M4 17.5h1m1 0h1m1 0h1m2 0h1m1 0h2m1 0h1m4 0h1m1 0h1m1 0h1m1 0h1M4 18.5h1m1 0h1m1 0h1m1 0h2m7 0h7m1 0h2M4 19.5h1m1 0h1m1 0h2m1 0h2m3 0h1m1 0h3m1 0h3m3 0h1M4 20.5h1m1 0h3m1 0h2m1 0h1m2 0h9m1 0h1M12 21.5h2m3 0h1m1 0h2m3 0h2M4 22.5h7m4 0h2m1 0h1m1 0h1m1 0h1m1 0h1m1 0h3M4 23.5h1m5 0h1m1 0h1m2 0h1m4 0h1m3 0h2m2 0h1M4 24.5h1m1 0h3m1 0h1m1 0h2m1 0h10m1 0h1M4 25.5h1m1 0h3m1 0h1m1 0h2m2 0h2m1 0h1m1 0h2m1 0h5M4 26.5h1m1 0h3m1 0h1m1 0h1m4 0h1m2 0h1m4 0h2m1 0h1M4 27.5h1m5 0h1m2 0h4m1 0h3m1 0h4m2 0h1M4 28.5h7m1 0h1m1 0h1m2 0h2m2 0h8"/>
            </svg>
          </div>
          <div class="text-[10px] text-amber-300 font-mono font-bold">
            Scan for Portfolio & Talks
          </div>
          <a href="https://netale.et/#talks" target="_blank" class="text-[9px] text-slate-400 hover:text-white underline font-mono">
            netale.et/#talks
          </a>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/WrapUpSlide.vue", "w") as f:
    f.write(wrap_up)

print("Updated HotwireInteractionSlide, WrapUpSlide")
