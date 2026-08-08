<template>
  <div class="react-native-case-study-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '💬 親身經驗' : '💬 Personal Experience' }}</span>
      <span class="text-xs font-mono text-slate-400">Client Project: Crave Robotics</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-4 text-left">
      <template v-if="currentLang === 'zh'">
        真實案例：<span class="text-red-500">React Native 的 API 同步代價 ⚡</span>
      </template>
      <template v-else>
        Real Story: <span class="text-red-500">The React Native API Tax ⚡</span>
      </template>
    </h2>

    <!-- 2 Column Layout -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-5 items-center">
      
      <!-- Left Column: Discord Screenshot Frame (Cols 1-7) -->
      <div class="md:col-span-7 space-y-2 text-left">
        <div class="bg-slate-900 border-2 border-red-500/40 rounded-2xl p-2 shadow-2xl relative overflow-hidden group">
          <div class="bg-slate-950 px-3 py-1.5 rounded-t-xl border-b border-slate-800 flex items-center justify-between text-[11px] font-mono text-slate-300 mb-2">
            <span class="flex items-center gap-2 font-bold text-red-400">
              <span class="w-2.5 h-2.5 rounded-full bg-red-500 animate-pulse"></span>
              #crave-robotics-api (Discord)
            </span>
            <span class="text-[10px] text-slate-500">Stripe Integration Issue</span>
          </div>

          <div class="rounded-xl overflow-hidden border border-slate-800 bg-black/60">
            <img 
              src="/crave_robotics_discord.png" 
              alt="Crave Robotics Discord API Mismatch Issue" 
              class="w-full object-cover rounded-lg"
            />
          </div>
        </div>

        <div class="text-[10px] font-mono text-slate-400 flex items-center gap-1.5 pl-1">
          <span class="text-amber-400">⚠️</span>
          <span>{{ currentLang === 'zh' ? '客戶專案中的真實 Discord 除錯對話紀錄' : 'Actual Discord debug log from my client project with Crave Robotics' }}</span>
        </div>
      </div>

      <!-- Right Column: 2 Simple Points (Cols 8-12) -->
      <div class="md:col-span-5 space-y-4 text-left">
        <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-4 shadow-xl space-y-1.5">
          <h4 class="text-sm font-bold text-red-400 m-0 flex items-center gap-1.5">
            <span>⚡ {{ currentLang === 'zh' ? 'API Key 與環境脫節' : 'API Key & Environment Desync' }}</span>
          </h4>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            {{ currentLang === 'zh' ? '後端更新了 Stripe 金鑰，結果無聲無息地導致 React Native 手機端刷卡失效。' : 'Backend changed Stripe publishable keys & accounts, breaking card tokenization silently on the React Native mobile app.' }}
          </p>
        </div>

        <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-4 shadow-xl space-y-1.5">
          <h4 class="text-sm font-bold text-amber-400 m-0 flex items-center gap-1.5">
            <span>🗣️ {{ currentLang === 'zh' ? '溝通耗時' : 'Communication Overhead' }}</span>
          </h4>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            {{ currentLang === 'zh' ? '後端工程師與 React Native 手機工程師浪費無數小時比對 API 格式與金鑰。' : 'Hours wasted cross-checking API logs between backend devs and mobile React Native devs just to align endpoints and keys.' }}
          </p>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
