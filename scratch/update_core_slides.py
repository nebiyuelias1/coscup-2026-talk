import os

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

# 1. IdeaToRealitySlide.vue
idea_to_reality = '''<template>
  <div class="idea-to-reality-slide w-full my-auto flex flex-col justify-center text-left">
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '💡 產品旅程' : '💡 Product Journey' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '從零到一' : 'From Zero to One' }}</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-6">
      <template v-if="currentLang === 'zh'">
        從點子到上線：<span class="text-red-500">Rails 單體架構 🚀</span>
      </template>
      <template v-else>
        From Idea to Reality: <span class="text-red-500">The Rails Way 🚀</span>
      </template>
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-6">
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-3xl">🛠️</span>
        <h3 class="text-base font-bold text-white m-0">{{ currentLang === 'zh' ? '單人開發火力' : 'Solo Developer Power' }}</h3>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          {{ currentLang === 'zh' ? '1 位工程師便能獨自處理全棧、資料庫、後端與前端介面。' : '1 engineer handles DB, backend, and web UI effortlessly.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-3xl">⚡</span>
        <h3 class="text-base font-bold text-white m-0">{{ currentLang === 'zh' ? '極速疊代驗證' : 'Rapid Validation' }}</h3>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          {{ currentLang === 'zh' ? '幾天內就能驗證產品點子並推向市場收集反饋。' : 'Validate product ideas and launch web apps in days.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-5 shadow-xl space-y-2 bg-red-950/10">
        <span class="text-3xl">📈</span>
        <h3 class="text-base font-bold text-white m-0">{{ currentLang === 'zh' ? '獲得市場 Traction' : 'Hits Traction' }}</h3>
        <p class="text-xs text-slate-300 leading-relaxed m-0">
          {{ currentLang === 'zh' ? '使用者開始大量湧入，需求爆發！' : 'Users flood in, generating massive engagement!' }}
        </p>
      </div>
    </div>

    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-300">
        ✨ <strong>Rails Advantage:</strong> {{ currentLang === 'zh' ? '單體架構帶來極高效率，讓小團隊專注打造產品。' : 'The monolithic speed allows small teams to move ridiculously fast.' }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/IdeaToRealitySlide.vue", "w") as f:
    f.write(idea_to_reality)

# 2. MobileRequirementSlide.vue
mobile_req = '''<template>
  <div class="mobile-requirement-slide w-full my-auto flex flex-col justify-center text-left">
    <div class="flex justify-between items-center mb-2">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '⚠️ 抉擇時刻' : '⚠️ The Dilemma' }}</span>
      <span class="text-xs font-mono text-slate-400">{{ currentLang === 'zh' ? '跨平台挑戰' : 'Cross-Platform Challenge' }}</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-5">
      <template v-if="currentLang === 'zh'">
        我們需要 <span class="text-red-500">Mobile Apps</span>... 該怎麼做？ 🤔
      </template>
      <template v-else>
        We Need <span class="text-red-500">Mobile Apps</span>... Now What? 🤔
      </template>
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-5">
      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-2xl">🌐</span>
        <h3 class="text-sm font-bold text-amber-400 m-0">Option A: PWA</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '快速但受限：缺乏 App Store 上架與完整原生能力。' : 'Fast but limited: Lacks App Store presence & full native capabilities.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-2xl">⚛️</span>
        <h3 class="text-sm font-bold text-cyan-400 m-0">Option B: React Native / Flutter</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '強大但高昂：需重寫所有前端與 logic，維護雙重 Codebase。' : 'Powerful but expensive: Duplicate business logic & components.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-5 shadow-xl space-y-2">
        <span class="text-2xl">🍎🤖</span>
        <h3 class="text-sm font-bold text-purple-400 m-0">Option C: Swift & Kotlin</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '頂級體驗但成本巨大：需招募 2 個獨立的原生開發團隊。' : 'Top experience but maximum cost: Requires 2 dedicated native teams.' }}
        </p>
      </div>
    </div>

    <div class="p-3 bg-red-950/30 border border-red-500/30 rounded-xl text-xs flex items-center justify-between">
      <span class="text-slate-200">
        💡 <strong>{{ currentLang === 'zh' ? '問題根源:' : 'The Core Problem:' }}</strong> {{ currentLang === 'zh' ? '資源與人力有限時，重複開發只會拖慢腳步。' : 'Small teams cannot afford duplicating business logic across 3 codebases.' }}
      </span>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/MobileRequirementSlide.vue", "w") as f:
    f.write(mobile_req)

# 3. RailsContrarianSlide.vue
rails_contrarian = '''<template>
  <div class="rails-contrarian-slide w-full my-auto flex flex-col justify-center text-left">
    
    <!-- Progress Indicator Bar for single pillar slides -->
    <div v-if="pillar && pillar !== 'all'" class="mb-2">
      <div class="flex items-center justify-between mb-1">
        <span class="rails-badge font-bold text-xs">🥊 {{ currentLang === 'zh' ? 'Rails 核心哲學' : 'The Rails Philosophy' }}</span>
        <span class="text-[11px] font-mono text-amber-300 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-500/40">
          {{ currentLang === 'zh' ? '觀點' : 'Point' }} {{ currentPillarIndex }} / 4 🎯
        </span>
      </div>

      <!-- 4-Segment Progress Bar -->
      <div class="grid grid-cols-4 gap-2">
        <div 
          v-for="idx in [1, 2, 3, 4]" 
          :key="idx"
          :class="[
            'h-1 rounded-full transition-all',
            idx <= currentPillarIndex ? 'bg-red-500 shadow-sm shadow-red-500/50' : 'bg-slate-800'
          ]"></div>
      </div>
    </div>

    <!-- Header for Overview Slide -->
    <div v-else class="flex justify-between items-center mb-1">
      <span class="rails-badge font-bold text-xs">🥊 {{ currentLang === 'zh' ? 'Rails 核心哲學' : 'The Rails Philosophy' }}</span>
      <span class="text-[11px] font-mono text-slate-400">{{ currentLang === 'zh' ? '實用主義勝過過度包裝' : 'Pragmatism Over Hype' }}</span>
    </div>

    <!-- Main Title -->
    <h2 class="text-xl font-black tracking-tight text-white mb-3 flex items-center justify-between">
      <span>{{ currentLang === 'zh' ? '擁抱' : 'Embrace Being' }} <span class="text-red-500">{{ currentLang === 'zh' ? '逆向思考 (Contrarian) 🎯' : 'Contrarian 🎯' }}</span></span>
      <span v-if="!pillar || pillar === 'all'" class="text-[11px] font-mono text-amber-300 bg-amber-950/80 px-2 py-0.5 rounded border border-amber-500/40">
        {{ currentLang === 'zh' ? '極簡 > 炒作 ⚡' : 'Simplicity > Hype ⚡' }}
      </span>
    </h2>

    <!-- SINGLE PILLAR SLIDE VIEW -->

    <!-- Point 1: Solid Cache & Queue -->
    <template v-if="pillar === 'solid'">
      <div class="bg-slate-900/90 border-2 border-red-500/40 rounded-xl p-4 shadow-xl space-y-2.5">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">🗄️</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">1. Solid Cache & Solid Queue</h3>
              <p class="text-[11px] text-red-400 font-mono m-0">{{ currentLang === 'zh' ? '將資料庫作為核心基礎設施' : 'Database as Infrastructure' }}</p>
            </div>
          </div>
          <span class="px-2.5 py-0.5 bg-red-950 text-red-300 border border-red-800 rounded-full text-[11px] font-mono font-bold">
            {{ currentLang === 'zh' ? '零額外基礎設施' : 'Zero Extra Infra' }}
          </span>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            {{ currentLang === 'zh' ? '"你必須為了快取和背景任務建立額外的 Redis、Memcached 與複雜集群！"' : '"You must run Redis, Memcached, and complex RAM server clusters just for caching and background jobs."' }}
          </p>
        </div>

        <div class="p-3 bg-red-950/40 border border-red-500/30 rounded-lg">
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            {{ currentLang === 'zh' ? '直接利用現有的 SQL 資料庫處理快取 (SolidCache) 與背景任務 (SolidQueue)。零額外 RAM 集群，零額外維運負擔。' : 'Use your existing SQL database for caching (SolidCache) and background jobs (SolidQueue). Zero extra RAM clusters, zero extra DevOps maintenance.' }}
          </p>
        </div>
      </div>
    </template>

    <!-- Point 2: Schema Introspection -->
    <template v-if="pillar === 'schema'">
      <div class="bg-slate-900/90 border-2 border-amber-500/40 rounded-xl p-4 shadow-xl space-y-2.5">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">🔍</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">2. Schema Introspection</h3>
              <p class="text-[11px] text-amber-400 font-mono m-0">ActiveRecord Runtime Magic</p>
            </div>
          </div>
          <span class="px-2.5 py-0.5 bg-amber-950 text-amber-300 border border-amber-800 rounded-full text-[11px] font-mono font-bold">
            {{ currentLang === 'zh' ? '零冗餘樣板程式碼' : 'Zero Boilerplate' }}
          </span>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            {{ currentLang === 'zh' ? '"手動在 ORM、DTO 與型別定義之間重複宣告並同步資料庫的每一個欄位。"' : '"Manually define, duplicate, and sync every database model property across ORMs, DTOs, and type definitions."' }}
          </p>
        </div>

        <div class="p-3 bg-amber-950/40 border border-amber-500/30 rounded-lg">
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            {{ currentLang === 'zh' ? 'ActiveRecord 在啟動時自動探索資料庫 Schema。無需聲明樣板屬性，徹底避免 Schema 脫節，極大化開發效率。' : 'ActiveRecord inspects the database schema automatically at boot time. Zero boilerplate model declarations, zero schema drift, and maximum developer efficiency.' }}
          </p>
        </div>
      </div>
    </template>

    <!-- Point 3: Majestic Monolith -->
    <template v-if="pillar === 'monolith'">
      <div class="bg-slate-900/90 border-2 border-purple-500/40 rounded-xl p-4 shadow-xl space-y-2.5">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">🏰</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">3. Majestic Monolith (宏偉單體)</h3>
              <p class="text-[11px] text-purple-300 font-mono m-0">1 Developer Powerhouse</p>
            </div>
          </div>
          <span class="px-2.5 py-0.5 bg-purple-950 text-purple-300 border border-purple-800 rounded-full text-[11px] font-mono font-bold">
            {{ currentLang === 'zh' ? '10x 交付速度' : '10x Delivery Speed' }}
          </span>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            {{ currentLang === 'zh' ? '"在產品初期就將應用切分成 50 個 Kubernetes 微服務並引入複雜的分散式架構！"' : '"Split your early app into 50 Kubernetes microservices with distributed tracing and API gateways."' }}
          </p>
        </div>

        <div class="p-3 bg-purple-950/40 border border-purple-500/30 rounded-lg">
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            {{ currentLang === 'zh' ? '一個完整的 Rails 單體包含所有商業邏輯。單人開發者能在幾分鐘內完成構建、測試與部署，無需跨團隊溝通耗時。' : 'One cohesive Rails monolith contains all your business logic. 1 developer can build, test, and deploy features in minutes instead of waiting on cross-team coordination.' }}
          </p>
        </div>
      </div>
    </template>

    <!-- Point 4: HTML Over The Wire -->
    <template v-if="pillar === 'hotwire'">
      <div class="bg-slate-900/90 border-2 border-emerald-500/40 rounded-xl p-4 shadow-xl space-y-2.5">
        <div class="flex items-center justify-between border-b border-slate-800 pb-2">
          <div class="flex items-center gap-2.5">
            <span class="text-2xl">⚡</span>
            <div>
              <h3 class="text-lg font-black text-white m-0">4. HTML Over The Wire (Hotwire)</h3>
              <p class="text-[11px] text-emerald-400 font-mono m-0">{{ currentLang === 'zh' ? '統一 Web 與 Mobile 架構' : 'Web + Mobile Unified' }}</p>
            </div>
          </div>
          <span class="px-2.5 py-0.5 bg-emerald-950 text-emerald-300 border border-emerald-800 rounded-full text-[11px] font-mono font-bold">
            Hotwire Native
          </span>
        </div>

        <div class="p-2.5 bg-slate-950/80 border border-slate-800 rounded-lg">
          <p class="text-xs text-slate-300 line-through m-0">
            {{ currentLang === 'zh' ? '"開發獨立的 SPA 前端、REST API 層，並為 iOS 與 Android 重新用原生元件編寫全套 UI。"' : '"Build separate SPA frontend apps, REST API layers, and rewrite all UI components natively for iOS & Android."' }}
          </p>
        </div>

        <div class="p-3 bg-emerald-950/40 border border-emerald-500/30 rounded-lg">
          <p class="text-xs text-slate-100 leading-relaxed m-0 font-medium">
            {{ currentLang === 'zh' ? '在伺服器端渲染 HTML 並直接串流傳輸至原生外殼中。一套 Rails Codebase 同時驅動 Web、iOS 與 Android！' : 'Render HTML on the server and stream directly inside native mobile shells. Power your Web app, iOS app, and Android app simultaneously from 1 Rails codebase!' }}
          </p>
        </div>
      </div>
    </template>

    <!-- OVERVIEW SLIDE (Pillar == 'all' or default) -->
    <template v-if="!pillar || pillar === 'all'">
      <div class="grid grid-cols-1 md:grid-cols-2 gap-2.5 mb-2.5 text-left">
        <!-- 1. Solid Cache / Queue -->
        <div class="bg-slate-900/90 border border-red-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs font-bold text-red-400 flex items-center gap-1">
                🗄️ Solid Cache & Queue
              </span>
              <span class="text-[9px] font-mono bg-red-950 text-red-300 px-1.5 py-0.5 rounded border border-red-800">
                {{ currentLang === 'zh' ? '資料庫即基礎設施' : 'Database as Infra' }}
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              {{ currentLang === 'zh' ? '使用 SQL 資料庫處理快取與背景任務 (SolidCache / SolidQueue)。' : 'Use SQL database for cache & background jobs (SolidCache / SolidQueue).' }}
            </p>
          </div>
        </div>

        <!-- 2. ActiveRecord Introspection -->
        <div class="bg-slate-900/90 border border-amber-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs font-bold text-amber-400 flex items-center gap-1">
                🔍 Schema Introspection
              </span>
              <span class="text-[9px] font-mono bg-amber-950 text-amber-300 px-1.5 py-0.5 rounded border border-amber-800">
                {{ currentLang === 'zh' ? '零樣板程式碼' : 'Zero Boilerplate' }}
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              {{ currentLang === 'zh' ? 'ActiveRecord 在運行時自動探索資料庫 Schema。' : 'ActiveRecord inspects database schema automatically at runtime.' }}
            </p>
          </div>
        </div>

        <!-- 3. Majestic Monolith -->
        <div class="bg-slate-900/90 border border-purple-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs font-bold text-purple-300 flex items-center gap-1">
                🏰 Majestic Monolith
              </span>
              <span class="text-[9px] font-mono bg-purple-950 text-purple-300 px-1.5 py-0.5 rounded border border-purple-800">
                {{ currentLang === 'zh' ? '單人開發效率' : 'Solo Dev Speed' }}
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              {{ currentLang === 'zh' ? '一套專注的 Codebase 驅動完整的 Web 與 Mobile 產品。' : 'One cohesive codebase powers your entire web & mobile product.' }}
            </p>
          </div>
        </div>

        <!-- 4. HTML Over The Wire -->
        <div class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-3 shadow-lg flex flex-col justify-between">
          <div>
            <div class="flex items-center justify-between mb-1">
              <span class="text-xs font-bold text-emerald-400 flex items-center gap-1">
                ⚡ HTML Over The Wire
              </span>
              <span class="text-[9px] font-mono bg-emerald-950 text-emerald-300 px-1.5 py-0.5 rounded border border-emerald-800">
                Hotwire Native
              </span>
            </div>
            <p class="text-[11px] text-slate-200 leading-snug m-0">
              {{ currentLang === 'zh' ? '在伺服器端渲染 HTML 並即時串流至原生 App 容器中。' : 'Render HTML on server & stream directly inside native mobile shells.' }}
            </p>
          </div>
        </div>
      </div>
    </template>

    <!-- Bottom Takeaway Banner -->
    <div class="mt-2 p-2.5 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between text-[11px]">
      <span class="text-slate-300">
        💡 <strong>{{ currentLang === 'zh' ? '核心祕訣:' : 'The Secret:' }}</strong> {{ currentLang === 'zh' ? '逆向思考不是盲目固執 — 而是選擇「交付速度勝過過度複雜」。' : "Being contrarian isn't about being stubborn — it's about choosing shipping speed over complexity." }}
      </span>
      <span class="text-[10px] font-mono text-red-400 bg-red-950/80 px-2 py-0.5 rounded border border-red-700 shrink-0 font-bold ml-2">
        {{ currentLang === 'zh' ? 'Rails 獨特優勢 💎' : 'The Rails Advantage 💎' }}
      </span>
    </div>

  </div>
</template>

<script setup>
import { computed } from 'vue'
import { currentLang } from '../composables/useLang'

const props = defineProps({
  pillar: {
    type: String,
    default: null
  }
})

const currentPillarIndex = computed(() => {
  switch (props.pillar) {
    case 'solid': return 1
    case 'schema': return 2
    case 'monolith': return 3
    case 'hotwire': return 4
    default: return 0
  }
})
</script>
'''

with open(f"{components_dir}/RailsContrarianSlide.vue", "w") as f:
    f.write(rails_contrarian)

print("Updated IdeaToRealitySlide, MobileRequirementSlide, RailsContrarianSlide")
