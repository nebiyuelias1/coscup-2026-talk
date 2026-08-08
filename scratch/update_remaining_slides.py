import os

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

# AlternativesSlide.vue
alternatives_slide = '''<template>
  <div class="alternatives-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Progress Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '⚔️ 架構方案比較' : '⚔️ Architecture Tradeoffs' }}</span>
      <span class="text-xs font-mono text-slate-400">
        {{ currentLang === 'zh' ? '評估選項' : 'Evaluating Option' }} {{ currentStepIndex }} / 3
      </span>
    </div>

    <!-- Main Title -->
    <h2 class="text-2xl font-black tracking-tight text-white mb-4">
      <template v-if="approach === 'pwa'">
        {{ currentLang === 'zh' ? '評估 PWA (Progressive Web App) 🌐' : 'Evaluating PWA (Progressive Web App) 🌐' }}
      </template>
      <template v-else-if="approach === 'react-native'">
        {{ currentLang === 'zh' ? '評估 React Native / Flutter ⚛️' : 'Evaluating React Native / Flutter ⚛️' }}
      </template>
      <template v-else>
        {{ currentLang === 'zh' ? '評估純原生 (Swift & Kotlin) 🍎🤖' : 'Evaluating Pure Native (Swift & Kotlin) 🍎🤖' }}
      </template>
    </h2>

    <!-- Single Approach Focus Card -->
    <div class="bg-slate-900/90 border-2 rounded-2xl p-5 shadow-2xl space-y-4 mb-4"
         :class="{
           'border-amber-500/40': approach === 'pwa',
           'border-cyan-500/40': approach === 'react-native',
           'border-purple-500/40': approach === 'native'
         }">
      
      <!-- Option Header -->
      <div class="flex items-center justify-between border-b border-slate-800 pb-3">
        <div class="flex items-center gap-3">
          <span class="text-3xl">
            <template v-if="approach === 'pwa'">🌐</template>
            <template v-else-if="approach === 'react-native'">⚛️</template>
            <template v-else>📱</template>
          </span>
          <div>
            <h3 class="text-lg font-black text-white m-0">
              <template v-if="approach === 'pwa'">PWA (Progressive Web App)</template>
              <template v-else-if="approach === 'react-native'">React Native / Flutter</template>
              <template v-else>Pure Native (Swift + Kotlin)</template>
            </h3>
            <p class="text-xs font-mono m-0"
               :class="{
                 'text-amber-400': approach === 'pwa',
                 'text-cyan-400': approach === 'react-native',
                 'text-purple-400': approach === 'native'
               }">
              <template v-if="approach === 'pwa'">{{ currentLang === 'zh' ? '網頁打包容器' : 'Web Packaged Shell' }}</template>
              <template v-else-if="approach === 'react-native'">{{ currentLang === 'zh' ? '跨平台 JS/Dart 框架' : 'Cross-Platform Framework' }}</template>
              <template v-else>{{ currentLang === 'zh' ? '雙重原生開發' : 'Dual Native Engineering' }}</template>
            </p>
          </div>
        </div>
      </div>

      <!-- Pros & Cons Grid -->
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <!-- Pros -->
        <div class="p-3.5 bg-emerald-950/30 border border-emerald-500/30 rounded-xl space-y-1">
          <div class="text-xs font-bold text-emerald-400 uppercase tracking-wider flex items-center gap-1">
            <span>✅</span> {{ currentLang === 'zh' ? '優點' : 'Pros' }}
          </div>
          <p class="text-xs text-slate-200 leading-relaxed m-0">
            <template v-if="approach === 'pwa'">
              {{ currentLang === 'zh' ? '開發極快，直接重用現有 Web code。無 App Store 審核延遲。' : 'Super fast to ship. Reuses web code. Zero App Store review delays.' }}
            </template>
            <template v-else-if="approach === 'react-native'">
              {{ currentLang === 'zh' ? '原生元件 UI 體驗佳，巨大的生態系與套件庫。' : 'Rich native UI components, great performance, huge ecosystem.' }}
            </template>
            <template v-else>
              {{ currentLang === 'zh' ? '無可匹敵的原生效能與全套 iOS/Android API 存取權限。' : '100% native performance, zero limits on device APIs, best UX.' }}
            </template>
          </p>
        </div>

        <!-- Cons -->
        <div class="p-3.5 bg-red-950/30 border border-red-500/30 rounded-xl space-y-1">
          <div class="text-xs font-bold text-red-400 uppercase tracking-wider flex items-center gap-1">
            <span>❌</span> {{ currentLang === 'zh' ? '缺點 / 代價' : 'Cons / Blockers' }}
          </div>
          <p class="text-xs text-slate-200 leading-relaxed m-0">
            <template v-if="approach === 'pwa'">
              {{ currentLang === 'zh' ? '缺少 App Store 曝光、iOS 推送限制、無法吸引習慣商店下載的用戶。' : 'No App Store presence, iOS push limits, missing native feel.' }}
            </template>
            <template v-else-if="approach === 'react-native'">
              {{ currentLang === 'zh' ? '需維護 2 套 Codebase，API 脫節問題，商業邏輯重複開發成本高。' : 'Requires maintaining separate frontend, sync issues, API duplication.' }}
            </template>
            <template v-else>
              {{ currentLang === 'zh' ? '需要 2 個獨立團隊 (Swift + Kotlin)，開發維護成本暴增 3 倍！' : 'Requires 2 dedicated native teams. Triples build & maintenance cost!' }}
            </template>
          </p>
        </div>
      </div>

    </div>

    <!-- Takeaway Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        💡 <strong>{{ currentLang === 'zh' ? '結論:' : 'Takeaway:' }}</strong> 
        <template v-if="approach === 'pwa'">
          {{ currentLang === 'zh' ? 'PWA 適合輕量工具，但無法滿足對 App Store 有強烈需求的用戶。' : 'PWA is great for internal tools, but misses App Store mobile demand.' }}
        </template>
        <template v-else-if="approach === 'react-native'">
          {{ currentLang === 'zh' ? 'React Native 強大，但對於小型 Rails 團隊來說維護成本過高。' : 'React Native is powerful, but adds massive maintenance overhead for Rails teams.' }}
        </template>
        <template v-else>
          {{ currentLang === 'zh' ? '純原生適合大企業，但小型團隊無力負擔 3 套 Codebase。' : 'Pure native is for tech giants — small teams cannot maintain 3 codebases.' }}
        </template>
      </span>
    </div>

  </div>
</template>

<script setup>
import { computed } from 'vue'
import { currentLang } from '../composables/useLang'

const props = defineProps({
  approach: {
    type: String,
    default: 'pwa'
  }
})

const currentStepIndex = computed(() => {
  switch (props.approach) {
    case 'pwa': return 1
    case 'react-native': return 2
    case 'native': return 3
    default: return 1
  }
})
</script>
'''

with open(f"{components_dir}/AlternativesSlide.vue", "w") as f:
    f.write(alternatives_slide)

print("AlternativesSlide updated")
