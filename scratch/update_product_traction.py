import os

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

# 1. ProductTractionSlide.vue
product_traction = '''<template>
  <div class="product-traction-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Header Badge -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '📈 增長與需求' : '📈 Growth & Demand' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '下一個里程碑' : 'The Next Milestone' }}</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-3xl font-black tracking-tight text-white mb-5">
      <template v-if="currentLang === 'zh'">
        業務獲得增長... 用戶開始渴望 <span class="text-red-500">Mobile App! 📱</span>
      </template>
      <template v-else>
        Traction Hits... & Users Demand <span class="text-red-500">Mobile! 📱</span>
      </template>
    </h2>

    <!-- User Feedback / Demand Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-5">
      
      <!-- Feedback 1: App Store -->
      <div class="bg-slate-900/90 border border-amber-500/40 rounded-2xl p-5 shadow-2xl flex flex-col justify-between space-y-4">
        <div class="space-y-2">
          <span class="text-2xl">💬</span>
          <h3 class="text-base font-bold text-white m-0">
            {{ currentLang === 'zh' ? '"請問有 App Store 下載連結嗎？"' : '"Is there an App Store link?"' }}
          </h3>
        </div>
        <span class="text-[10px] font-mono text-amber-400 bg-amber-950/80 px-2.5 py-1 rounded border border-amber-800 font-bold self-start">
          {{ currentLang === 'zh' ? '商店搜尋與信任' : 'App Store Discovery' }}
        </span>
      </div>

      <!-- Feedback 2: Push Notifications -->
      <div class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-5 shadow-2xl flex flex-col justify-between space-y-4">
        <div class="space-y-2">
          <span class="text-2xl">🔔</span>
          <h3 class="text-base font-bold text-white m-0">
            {{ currentLang === 'zh' ? '"可以發送 Push 推送通知給我嗎！"' : '"Send me Push Notifications!"' }}
          </h3>
        </div>
        <span class="text-[10px] font-mono text-red-400 bg-red-950/80 px-2.5 py-1 rounded border border-red-800 font-bold self-start">
          {{ currentLang === 'zh' ? '原生觸達互動' : 'Native Engagement' }}
        </span>
      </div>

      <!-- Feedback 3: Home Screen & Speed -->
      <div class="bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-5 shadow-2xl flex flex-col justify-between space-y-4">
        <div class="space-y-2">
          <span class="text-2xl">📲</span>
          <h3 class="text-base font-bold text-white m-0">
            {{ currentLang === 'zh' ? '"我想直接放在手機主畫面上！"' : '"I want an icon on my Home Screen!"' }}
          </h3>
        </div>
        <span class="text-[10px] font-mono text-emerald-400 bg-emerald-950/80 px-2.5 py-1 rounded border border-emerald-800 font-bold self-start">
          {{ currentLang === 'zh' ? '用戶留存率' : 'User Retention' }}
        </span>
      </div>

    </div>

    <!-- Bottom Takeaway Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        🚨 <strong>{{ currentLang === 'zh' ? '現實情況:' : 'The Reality:' }}</strong> {{ currentLang === 'zh' ? '當你的 Web 產品獲得成長，發佈 iOS/Android 原生 App 成為必經之路。' : 'As your web product grows, shipping native iOS & Android apps becomes mandatory for survival.' }}
      </span>
      <span class="text-[10px] font-mono text-amber-400 bg-amber-950/80 px-2.5 py-1 rounded border border-amber-800 font-bold shrink-0 ml-2">
        {{ currentLang === 'zh' ? '移動端強烈需求 📱' : 'Mobile Demand 📱' }}
      </span>
    </div>

  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/ProductTractionSlide.vue", "w") as f:
    f.write(product_traction)

print("ProductTractionSlide updated")
