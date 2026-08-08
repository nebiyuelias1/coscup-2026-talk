<template>
  <div class="slido-qa-slide w-full h-full my-auto flex flex-col justify-center text-left py-2">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <div class="flex items-center gap-2">
        <span class="rails-badge font-bold">💬 Slido Live Q&A</span>
        <div class="title-chip flex items-center gap-1 text-[10px]">
          <img src="/coscup_logo.png" alt="COSCUP Logo" class="h-3 object-contain" />
          <span>COSCUP 2026</span>
        </div>
      </div>
      
      <!-- Open in New Tab Button -->
      <a
        href="https://wall.sli.do/event/3NNNoWL8UJUnYz7LsmyzfM?section=ec4f745a-3fbc-4151-9ece-ab8d5e325f3b&integration=shared-present-mode&utm_source=slidoadmin"
        target="_blank"
        class="bg-red-600/90 hover:bg-red-500 text-white font-mono text-[11px] px-3 py-1 rounded-lg font-bold transition-all shadow flex items-center gap-1.5 cursor-pointer border border-red-500/40"
      >
        <span>{{ currentLang === 'zh' ? '↗ 新分頁開啟' : '↗ Open Fullscreen' }}</span>
      </a>
    </div>

    <!-- 2 Column Split Layout: Left QR Code Card, Right Embedded Live Slido Present Iframe -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-3 items-stretch flex-1 min-h-0">
      
      <!-- Left Column: Scan QR Code (Cols 1-4) -->
      <div class="md:col-span-4 bg-slate-900/90 border-2 border-red-500/40 rounded-2xl p-4 shadow-xl backdrop-blur-md flex flex-col justify-between items-center text-center">
        <div>
          <h3 class="text-base font-black text-white mb-1">
            {{ currentLang === 'zh' ? '掃描 QR Code 提問 📱' : 'Scan to Submit Question 📱' }}
          </h3>
          <p class="text-[11px] text-slate-300 leading-snug mb-3">
            {{ currentLang === 'zh'
              ? '使用手機掃描下方 QR Code，即可加入 Slido 提問與投票！'
              : 'Scan with your phone to post questions or upvote existing ones.' }}
          </p>
        </div>

        <!-- Scannable QR Code Image -->
        <div class="w-40 h-40 bg-white p-2 rounded-2xl shadow-xl flex items-center justify-center border border-slate-700 my-auto">
          <img 
            src="/qr_coscup_2026_q_a.png" 
            alt="Slido Q&A QR Code" 
            class="w-full h-full object-contain rounded-xl"
          />
        </div>

        <div class="mt-3 text-[10px] font-mono text-amber-300 font-bold bg-amber-950/60 px-2.5 py-1 rounded-md border border-amber-800/60">
          slido #COSCUP2026 ⚡
        </div>
      </div>

      <!-- Right Column: Embedded Live Slido Presenter Display (Cols 5-12) -->
      <div class="md:col-span-8 bg-slate-950 border border-slate-800 rounded-2xl overflow-hidden shadow-2xl flex flex-col">
        <iframe
          src="https://wall.sli.do/event/3NNNoWL8UJUnYz7LsmyzfM?section=ec4f745a-3fbc-4151-9ece-ab8d5e325f3b&integration=shared-present-mode&utm_source=slidoadmin"
          class="w-full h-full min-h-[360px] border-0 rounded-2xl bg-slate-950"
          frameborder="0"
          allow="fullscreen"
          title="Slido Live Questions Display"
        ></iframe>
      </div>

    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
