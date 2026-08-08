import os

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

# 1. ReactNativeCaseStudySlide.vue
react_native_case = '''<template>
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
'''

with open(f"{components_dir}/ReactNativeCaseStudySlide.vue", "w") as f:
    f.write(react_native_case)

# 2. SmallTeamIdeaSlide.vue
small_team_slide = '''<template>
  <div class="small-team-idea-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '💡 靈光一閃' : '💡 The Lightbulb Moment' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '小團隊策略' : 'Small Team Strategy' }}</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-3 text-left">
      <template v-if="currentLang === 'zh'">
        等等... 我們是 <span class="text-red-500">小團隊！ 🚀</span>
      </template>
      <template v-else>
        But Wait... We're a <span class="text-red-500">Small Team! 🚀</span>
      </template>
    </h2>

    <p class="text-sm text-slate-300 text-left mb-5">
      {{ currentLang === 'zh'
        ? '如果我們能直接利用「現有的 Rails Web App」來構建我們的原生手機 App 呢？'
        : 'What if we can use the Rails app we already have to also build our mobile app?' }}
    </p>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/SmallTeamIdeaSlide.vue", "w") as f:
    f.write(small_team_slide)

# 3. WebviewMythsSlide.vue
webview_myths_slide = '''<template>
  <div class="webview-myths-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '🗣️ 技術圈偏見' : '🗣️ Tech Industry Dogma' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '刻板印象 vs 現實' : 'Conventional Wisdom vs Reality' }}</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-4 text-center">
      <template v-if="currentLang === 'zh'">
        接著主流工程師開始質疑... <span class="text-red-500">🙄</span>
      </template>
      <template v-else>
        Then The "Cool Kids" <span class="text-red-500">Speak Up... 🙄</span>
      </template>
    </h2>

    <!-- Centered Hero Image Frame -->
    <div class="max-w-2xl mx-auto w-full my-2">
      <div class="bg-slate-900 border-2 border-purple-500/40 rounded-2xl p-2.5 shadow-2xl relative overflow-hidden group">
        <div class="rounded-xl overflow-hidden border border-slate-800 bg-black relative">
          <img 
            src="/mean_girls.png" 
            alt="Mean Girls Judging Movie Still" 
            class="w-full h-72 object-cover rounded-lg transform transition-transform group-hover:scale-[1.01]"
          />

          <!-- Speech Bubble Overlay -->
          <div class="absolute top-3 left-1/2 -translate-x-1/2 bg-slate-950/95 border-2 border-pink-500/80 backdrop-blur-md px-4 py-2 rounded-2xl shadow-2xl text-center z-20">
            <span class="text-xs md:text-sm font-bold text-pink-300 flex items-center gap-1.5 font-sans">
              💬 <em>{{ currentLang === 'zh' ? '"噁心... 你居然用 WebView？離我們遠一點！"' : '"Eww... a WebView? You can\'t deploy with us!"' }}</em> 💅
            </span>
          </div>

          <!-- Character Role Badges -->
          <div class="absolute bottom-3 left-3 bg-slate-950/90 border border-purple-500/70 backdrop-blur-md px-2.5 py-1 rounded-lg text-xs font-mono text-purple-300 z-10 font-bold shadow-lg">
            💅 Tech Twitter
          </div>

          <div class="absolute bottom-3 left-1/2 -translate-x-1/2 bg-pink-950/90 border-2 border-pink-400/80 backdrop-blur-md px-3 py-1 rounded-lg text-xs font-mono text-pink-200 z-10 font-bold shadow-xl">
            👑 Senior RN Architect
          </div>

          <div class="absolute bottom-3 right-3 bg-slate-950/90 border border-purple-500/70 backdrop-blur-md px-2.5 py-1 rounded-lg text-xs font-mono text-purple-300 z-10 font-bold shadow-lg">
            📦 SPA Purist
          </div>
        </div>
      </div>

      <div class="text-xs font-mono text-purple-300 flex items-center justify-between px-2 mt-2">
        <span>🎬 Mean Girls (2004)</span>
        <span class="text-slate-400">{{ currentLang === 'zh' ? '移動端開發社群刻板印象' : 'Mobile Dev Community Dogma' }}</span>
      </div>
    </div>

  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/WebviewMythsSlide.vue", "w") as f:
    f.write(webview_myths_slide)

# 4. WhatIsHotwireNativeSlide.vue
what_is_hotwire = '''<template>
  <div class="what-is-hotwire-slide w-full my-auto flex flex-col justify-center text-left">
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '🚀 核心解答' : '🚀 The Solution' }}</span>
      <span class="text-xs font-mono text-slate-400">Hybrid Magic</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-5">
      <template v-if="currentLang === 'zh'">
        什麼是 <span class="text-red-500">Hotwire Native？</span> 📱
      </template>
      <template v-else>
        What is <span class="text-red-500">Hotwire Native?</span> 📱
      </template>
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-5">
      <div class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-5 shadow-xl space-y-3">
        <span class="text-3xl">🌐</span>
        <h3 class="text-base font-bold text-white m-0">
          {{ currentLang === 'zh' ? '伺服器渲染 Web 頁面' : 'Server-Rendered Web' }}
        </h3>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          {{ currentLang === 'zh' ? '在 Rails 端處理大部分頁面與邏輯，更新即時生效，免去 App Store 重新審核！' : 'Render 90% of screens on the server. Instant updates without App Store reviews.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-5 shadow-xl space-y-3">
        <span class="text-3xl">⚡</span>
        <h3 class="text-base font-bold text-white m-0">
          {{ currentLang === 'zh' ? '原生導覽與外殼' : 'Native Shell & Navigation' }}
        </h3>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          {{ currentLang === 'zh' ? '原生導覽列、Tab Bar、推送通知與相機存取，帶來 100% 原生手機質感。' : 'Native navigation bars, tabs, push notifications, and camera access for native UX.' }}
        </p>
      </div>
    </div>

    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        💡 <strong>{{ currentLang === 'zh' ? '最佳組合:' : 'Best of Both Worlds:' }}</strong> {{ currentLang === 'zh' ? 'Web 的開發速度 + 原生 App 的優質體驗。' : 'Web speed of development combined with native user experience.' }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/WhatIsHotwireNativeSlide.vue", "w") as f:
    f.write(what_is_hotwire)

# 5. PortfolioTalksSlide.vue
portfolio_slide = '''<template>
  <div class="portfolio-talks-slide w-full my-auto flex flex-col justify-center text-center">
    <div class="mb-4">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '🎉 感謝大家！' : '🎉 Thank You!' }}</span>
    </div>

    <h2 class="text-4xl font-black tracking-tight text-white mb-4">
      <template v-if="currentLang === 'zh'">
        準備好用 Rails 發佈你的 <span class="text-red-500">Mobile App 嗎？ 🚀</span>
      </template>
      <template v-else>
        Ready to Ship Mobile Apps <span class="text-red-500">with Rails? 🚀</span>
      </template>
    </h2>

    <p class="text-lg text-slate-300 max-w-xl mx-auto mb-6">
      {{ currentLang === 'zh'
        ? '歡迎在 GitHub 關注專案，並探索我的研討會簡報與開源模版！'
        : 'Check out the GitHub repos, star the template, and let\'s build amazing products!' }}
    </p>

    <div class="flex items-center justify-center gap-4 flex-wrap text-sm">
      <a 
        href="https://github.com/nebiyuelias1" 
        target="_blank"
        class="bg-slate-900 hover:bg-slate-800 border border-slate-700 text-white font-mono px-4 py-2.5 rounded-xl font-bold transition-all shadow-lg flex items-center gap-2"
      >
        <span>🐙 GitHub: @nebiyuelias1</span>
      </a>
      <a 
        href="https://github.com/nebiyuelias1/turbo-rails-react-native-starter" 
        target="_blank"
        class="bg-red-600 hover:bg-red-500 text-white font-mono px-4 py-2.5 rounded-xl font-bold transition-all shadow-lg flex items-center gap-2"
      >
        <span>⭐ Hotwire Starter Template</span>
      </a>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/PortfolioTalksSlide.vue", "w") as f:
    f.write(portfolio_slide)

print("Updated ReactNativeCaseStudySlide, SmallTeamIdeaSlide, WebviewMythsSlide, WhatIsHotwireNativeSlide, PortfolioTalksSlide")
