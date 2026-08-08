import os

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

# 1. HotwireNativeIntroSlide.vue
hotwire_intro = '''<template>
  <div class="hotwire-intro-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-2">
      <span class="hotwire-badge">{{ currentLang === 'zh' ? '💡 解方誕生' : '💡 The Solution' }}</span>
      <span class="text-xs font-mono text-slate-400">HTML Over The Wire</span>
    </div>

    <h2 class="text-3xl font-black tracking-tight text-white mb-5 text-left">
      <template v-if="currentLang === 'zh'">
        隆重登場：<span class="text-red-500">Hotwire Native ⚡</span>
      </template>
      <template v-else>
        Enter <span class="text-red-500">Hotwire Native ⚡</span>
      </template>
    </h2>

    <!-- 3 Simple Punchy Cards -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-5">
      <!-- Point 1: 37signals -->
      <div class="bg-slate-900/90 border border-blue-500/30 rounded-2xl p-5 text-left shadow-xl flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-blue-600/20 text-blue-400 font-bold flex items-center justify-center text-xl mb-3">
            🏢
          </div>
          <h3 class="text-base font-bold text-white mb-1.5">{{ currentLang === 'zh' ? '37signals 打造' : 'Built by 37signals' }}</h3>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            {{ currentLang === 'zh' ? '專為 HEY 與 Basecamp 開發的實戰開源框架。' : 'Open-source framework built for HEY & Basecamp.' }}
          </p>
        </div>
        <div class="mt-4 pt-2 border-t border-slate-800 text-[10px] font-mono text-blue-300">
          {{ currentLang === 'zh' ? '生產環境千錘百鍊 🛡️' : 'Battle-tested in production 🛡️' }}
        </div>
      </div>

      <!-- Point 2: Send HTML -->
      <div class="bg-slate-900/90 border border-amber-500/30 rounded-2xl p-5 text-left shadow-xl flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-amber-600/20 text-amber-400 font-bold flex items-center justify-center text-xl mb-3">
            🌐
          </div>
          <h3 class="text-base font-bold text-white mb-1.5">{{ currentLang === 'zh' ? '直接傳送 HTML 至手機' : 'Send HTML to Mobile' }}</h3>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            {{ currentLang === 'zh' ? '伺服器渲染 HTML 畫面，直接呈現於原生 App 容器中。' : 'Server renders HTML views directly inside native mobile shells.' }}
          </p>
        </div>
        <div class="mt-4 pt-2 border-t border-slate-800 text-[10px] font-mono text-amber-300">
          {{ currentLang === 'zh' ? '無需繁瑣 JSON API ⚡' : 'No JSON APIs required ⚡' }}
        </div>
      </div>

      <!-- Point 3: Logic Stays on Server -->
      <div class="bg-slate-900/90 border border-red-500/30 rounded-2xl p-5 text-left shadow-xl flex flex-col justify-between">
        <div>
          <div class="w-10 h-10 rounded-xl bg-red-600/20 text-red-400 font-bold flex items-center justify-center text-xl mb-3">
            💎
          </div>
          <h3 class="text-base font-bold text-white mb-1.5">{{ currentLang === 'zh' ? '商業邏輯留存在 Server' : 'Logic Stays on Server' }}</h3>
          <p class="text-xs text-slate-300 leading-relaxed m-0">
            {{ currentLang === 'zh' ? '所有邏輯統一集中於 Rails。手機端保持極簡瘦身。' : 'All business logic remains in Rails. Mobile apps are thin clients.' }}
          </p>
        </div>
        <div class="mt-4 pt-2 border-t border-slate-800 text-[10px] font-mono text-red-300">
          {{ currentLang === 'zh' ? '零程式碼重複 🎯' : 'Zero code duplication 🎯' }}
        </div>
      </div>
    </div>

    <!-- Bottom Simple Banner -->
    <div class="p-3 bg-slate-950 border border-slate-800 rounded-xl flex items-center justify-between text-left px-4">
      <div class="flex items-center gap-2">
        <span class="text-base">🚀</span>
        <span class="text-xs text-slate-200 font-medium">
          {{ currentLang === 'zh' ? '寫 Ruby，渲染 HTML，部署至伺服器 — 一秒發佈至 Web, iOS 與 Android！' : 'Write Ruby. Render HTML. Deploy to server — instantly live on Web, iOS & Android.' }}
        </span>
      </div>
      <span class="text-[10px] font-mono text-emerald-300 bg-emerald-950/80 px-2.5 py-1 rounded border border-emerald-500/40 shrink-0 font-bold">
        Single Majestic Monolith ⚡
      </span>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/HotwireNativeIntroSlide.vue", "w") as f:
    f.write(hotwire_intro)

# 2. MonorepoSetupSlide.vue
monorepo_setup = '''<template>
  <div class="monorepo-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <h2
      class="text-2xl font-black tracking-tight text-white mb-2 text-left flex items-center justify-between"
    >
      <span
        >{{ currentLang === 'zh' ? 'Monorepo 專案架構:' : 'Monorepo Setup:' }}
        <span class="text-red-500">Rails + iOS + Android 📦</span></span
      >
    </h2>

    <!-- 2 Column Grid Layout -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
      <!-- Left Column: Directory Tree -->
      <div class="md:col-span-5 text-left">
        <div
          class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-xs text-slate-300 space-y-2"
        >
          <div
            class="flex items-center justify-between border-b border-slate-800 pb-2 text-[11px] text-slate-400"
          >
            <span class="flex items-center gap-1.5 text-white font-bold">
              <span
                class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"
              ></span>
              /
            </span>
            <span
              class="text-[10px] bg-slate-900 px-2 py-0.5 rounded text-amber-300"
              >{{ currentLang === 'zh' ? '根目錄' : 'Root Directory' }}</span
            >
          </div>

          <!-- Directory Tree Folders -->
          <div class="space-y-2 text-[11px]">
            <div
              @click="activeTab = 'backend'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'backend'
                  ? 'bg-red-950/50 border-red-500 ring-1 ring-red-500/50 shadow-lg translate-x-1'
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100',
              ]"
            >
              <div class="text-red-400 font-bold flex items-center gap-1.5">
                <span>💎 backend/</span>
              </div>
              <span
                class="text-[9px] bg-red-900/60 px-1.5 py-0.5 rounded text-red-200 font-mono"
                >Rails App</span
              >
            </div>

            <div
              @click="activeTab = 'ios'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'ios'
                  ? 'bg-blue-950/50 border-blue-500 ring-1 ring-blue-500/50 shadow-lg translate-x-1'
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100',
              ]"
            >
              <div class="text-blue-400 font-bold flex items-center gap-1.5">
                <span>🍏 ios/</span>
              </div>
              <span
                class="text-[9px] bg-blue-900/60 px-1.5 py-0.5 rounded text-blue-200 font-mono"
                >Swift App</span
              >
            </div>

            <div
              @click="activeTab = 'android'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'android'
                  ? 'bg-emerald-950/50 border-emerald-500 ring-1 ring-emerald-500/50 shadow-lg translate-x-1'
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100',
              ]"
            >
              <div class="text-emerald-400 font-bold flex items-center gap-1.5">
                <span>🤖 android/</span>
              </div>
              <span
                class="text-[9px] bg-emerald-900/60 px-1.5 py-0.5 rounded text-emerald-200 font-mono"
                >Kotlin App</span
              >
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Tabs -->
      <div class="md:col-span-7 text-left space-y-1.5">
        <div v-if="activeTab === 'backend'" class="space-y-1.5 animate-fade-in">
          <div
            class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1"
          >
            <span class="text-red-400 font-bold"
              >backend/ — Rails Monolith {{ currentLang === 'zh' ? '目錄結構' : 'Structure' }}</span
            >
          </div>

          <div
            class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto h-[240px] flex flex-col justify-between"
          >
            <div class="space-y-1 text-slate-300">
              <div class="text-red-400 font-bold">backend/</div>
              <div class="pl-3 text-slate-400">├── app/</div>
              <div class="pl-6 text-slate-400">├── controllers/</div>
              <div
                class="pl-9 text-amber-300 font-bold bg-amber-950/60 px-1.5 py-0.5 rounded border border-amber-800/60 inline-block"
              >
                └── configurations_controller.rb ⚡ (Path Config JSON)
              </div>
              <div class="pl-6 text-slate-400">
                └── views/ (Renders HTML for Web & Mobile)
              </div>
              <div class="pl-3 text-slate-400">├── config/routes.rb</div>
              <div class="pl-3 text-slate-400">└── Gemfile</div>
            </div>

            <div
              class="p-2 bg-slate-900 border border-slate-800 rounded text-[10px] text-amber-300"
            >
              <code
                >get "/configurations/ios_v1", to: "configurations#ios_v1"</code
              >
            </div>
          </div>
        </div>

        <div v-if="activeTab === 'ios'" class="space-y-1.5 animate-fade-in">
          <div
            class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1"
          >
            <span class="text-blue-400 font-bold"
              >ios/ — Swift Xcode {{ currentLang === 'zh' ? '目錄結構' : 'Project Structure' }}</span
            >
            <span
              class="bg-blue-950 text-blue-300 px-2 py-0.5 rounded text-[10px] border border-blue-800 font-bold"
              >iOS / Swift</span
            >
          </div>

          <div
            class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto h-[240px] flex flex-col justify-between"
          >
            <div class="space-y-1 text-slate-300">
              <div class="text-blue-400 font-bold">ios/</div>
              <div class="pl-3 text-slate-400">├── LitLoop.xcodeproj</div>
              <div class="pl-3 text-slate-400">└── App/</div>
              <div class="pl-6 text-slate-400">├── Delegates/</div>
              <div
                class="pl-9 text-blue-300 font-bold bg-blue-950/60 px-1.5 py-0.5 rounded border border-blue-800/60 inline-block"
              >
                ├── SceneDelegate.swift ⚡ (Hotwire Navigator Entry)
                <div>└── AppDelegate.swift</div>
              </div>
              <div class="pl-6 text-slate-400">└── Resources/</div>
              <div class="pl-9 text-slate-400">└── path_configuration.json</div>
            </div>

            <div
              class="p-2 bg-slate-900 border border-slate-800 rounded text-[10px] text-blue-300"
            >
              <code
                >Navigator(configuration: .init(name: "main", startLocation:
                baseURL))</code
              >
            </div>
          </div>
        </div>

        <div v-if="activeTab === 'android'" class="space-y-1.5 animate-fade-in">
          <div
            class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1"
          >
            <span class="text-emerald-400 font-bold"
              >android/ — Kotlin Gradle {{ currentLang === 'zh' ? '目錄結構' : 'Project Structure' }}</span
            >
            <span
              class="bg-emerald-950 text-emerald-300 px-2 py-0.5 rounded text-[10px] border border-emerald-800 font-bold"
              >Android / Kotlin</span
            >
          </div>

          <div
            class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto h-[240px] flex flex-col justify-between"
          >
            <div class="space-y-1 text-slate-300">
              <div class="text-emerald-400 font-bold">android/</div>
              <div class="pl-3 text-slate-400">├── build.gradle.kts</div>
              <div class="pl-3 text-slate-400">└── app/</div>
              <div class="pl-6 text-slate-400">
                ├── build.gradle.kts (dep: dev.hotwire:native)
              </div>
              <div class="pl-6 text-slate-400">
                └── src/main/java/et/netale/litloop/
              </div>
              <div
                class="pl-9 text-emerald-300 font-bold bg-emerald-950/60 px-1.5 py-0.5 rounded border border-emerald-800/60 inline-block"
              >
                └── MainActivity.kt ⚡ (HotwireActivity subclass)
              </div>
            </div>

            <div
              class="p-2 bg-slate-900 border border-slate-800 rounded text-[10px] text-emerald-300"
            >
              <code
                >class MainActivity : HotwireActivity() // startLocation =
                "https://litloop.club"</code
              >
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Bottom Takeaway Banner -->
    <div
      class="mt-3 p-2.5 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between text-xs"
    >
      <span class="text-slate-300">
        <template v-if="activeTab === 'backend'">
          💎 <strong>Rails Backend:</strong> {{ currentLang === 'zh' ? '存放 Model、Controller 與 ERB 視圖，並為手機端動態提供路由規則。' : 'Houses models, controllers & ERB views + serves dynamic navigation rules for mobile.' }}
        </template>
        <template v-if="activeTab === 'ios'">
          🍏 <strong>iOS Project:</strong> {{ currentLang === 'zh' ? '位於 /ios 資料夾下的 Xcode 專案，以 Swift SceneDelegate 作為入口。' : 'Xcode project inside /ios folder with Swift SceneDelegate entry.' }}
        </template>
        <template v-if="activeTab === 'android'">
          🤖 <strong>Android Project:</strong> {{ currentLang === 'zh' ? '位於 /android 資料夾下的 Gradle 專案，繼承 HotwireActivity。' : 'Gradle project inside /android folder extending HotwireActivity.' }}
        </template>
      </span>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import { currentLang } from '../composables/useLang'

const activeTab = ref("backend");
</script>

<style scoped>
@keyframes fadeIn {
  from {
    opacity: 0;
    transform: translateY(4px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

.animate-fade-in {
  animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>
'''

with open(f"{components_dir}/MonorepoSetupSlide.vue", "w") as f:
    f.write(monorepo_setup)

# 3. HotwireIosSetupSlide.vue
hotwire_ios = '''<template>
  <div class="hotwire-ios-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">{{ currentLang === 'zh' ? '🍏 iOS 原生整合' : '🍏 iOS Integration' }}</span>
      <span class="text-xs font-mono text-slate-400">Swift SDK</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left flex items-center justify-between">
      <span>{{ currentLang === 'zh' ? '整合 Hotwire Native 至 iOS' : 'Adding Hotwire Native to iOS' }} <span class="text-blue-400">(Swift) 🍏</span></span>
      
      <!-- Stepper Controls -->
      <div class="flex items-center gap-1.5 font-mono text-xs">
        <button 
          v-for="step in [1, 2, 3]" 
          :key="step"
          @click="activeStep = step"
          :class="[
            'px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold',
            activeStep === step 
              ? 'bg-blue-950/80 border-blue-500 text-blue-300 shadow-lg scale-105 ring-1 ring-blue-500/50' 
              : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'
          ]">
          {{ currentLang === 'zh' ? '步驟' : 'Step' }} {{ step }}
        </button>
      </div>
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      <div class="md:col-span-5 space-y-2.5">
        <div 
          @click="activeStep = 1"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 1 
              ? 'bg-slate-900 border-blue-500/60 shadow-lg ring-1 ring-blue-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 1 ? 'bg-blue-500/20 text-blue-400 border border-blue-500/40' : 'bg-slate-800 text-slate-400']">1</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">1. {{ currentLang === 'zh' ? '設定伺服器網址' : 'Define Base Server URL' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                {{ currentLang === 'zh' ? '設定 Rails App 伺服器端點。' : 'Set your Rails app base URL endpoint.' }}
              </p>
            </div>
          </div>
        </div>

        <div 
          @click="activeStep = 2"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 2 
              ? 'bg-slate-900 border-purple-500/60 shadow-lg ring-1 ring-purple-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 2 ? 'bg-purple-500/20 text-purple-300 border border-purple-500/40' : 'bg-slate-800 text-slate-400']">2</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">2. {{ currentLang === 'zh' ? '初始化 Hotwire Navigator' : 'Initialize Hotwire Navigator' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                {{ currentLang === 'zh' ? '建立指定起始畫面的 Navigator。' : 'Create Navigator(configuration:) with start location.' }}
              </p>
            </div>
          </div>
        </div>

        <div 
          @click="activeStep = 3"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 3 
              ? 'bg-slate-900 border-emerald-500/60 shadow-lg ring-1 ring-emerald-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 3 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' : 'bg-slate-800 text-slate-400']">3</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">3. {{ currentLang === 'zh' ? '綁定視窗與啟動路由' : 'Connect Window & Route' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                {{ currentLang === 'zh' ? '將 rootViewController 指向導航器並出發！' : 'Set rootViewController and trigger route(baseURL).' }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Code -->
      <div class="md:col-span-7 space-y-1.5">
        <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
          <span class="text-blue-400 font-bold">ios/App/Delegates/SceneDelegate.swift</span>
          <span class="bg-slate-900 text-blue-300 px-2 py-0.5 rounded text-[10px] border border-slate-800 font-bold">{{ currentLang === 'zh' ? '步驟' : 'Step' }} {{ activeStep }} / 3</span>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto leading-relaxed space-y-1 relative">
          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">
            <span class="text-purple-400">import</span> <span class="text-amber-300">HotwireNative</span><br/>
            <span class="text-purple-400">import</span> <span class="text-blue-300">UIKit</span>
          </div>

          <div :class="[
            'p-1.5 rounded transition-all duration-300',
            activeStep === 1 
              ? 'bg-blue-500/20 border-l-4 border-blue-400 text-white font-bold shadow-lg ring-1 ring-blue-500/30' 
              : 'opacity-30'
          ]">
            <span class="text-purple-400">let</span> baseURL = <span class="text-amber-300">URL</span>(string: <span class="text-emerald-300">"https://litloop.club/"</span>)!
          </div>

          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">
            <span class="text-purple-400">class</span> <span class="text-amber-300">SceneDelegate</span>: <span class="text-blue-300">UIResponder</span>, <span class="text-blue-300">UIWindowSceneDelegate</span> {<br/>
            &nbsp;&nbsp;<span class="text-purple-400">var</span> window: <span class="text-blue-300">UIWindow</span>?
          </div>

          <div :class="[
            'p-1.5 rounded transition-all duration-300 pl-4',
            activeStep === 2 
              ? 'bg-purple-500/20 border-l-4 border-purple-400 text-white font-bold shadow-lg ring-1 ring-purple-500/30' 
              : 'opacity-30'
          ]">
            <span class="text-purple-400">private let</span> navigator = <span class="text-amber-300">Navigator</span>(configuration: .init(<br/>
            &nbsp;&nbsp;&nbsp;&nbsp;name: <span class="text-emerald-300">"main"</span>, startLocation: baseURL.appending(path: <span class="text-emerald-300">"/"</span>)<br/>
            &nbsp;&nbsp;))
          </div>

          <div :class="['transition-opacity duration-300 pl-4', activeStep ? 'opacity-40' : '']">
            <span class="text-purple-400">func</span> <span class="text-blue-300">scene</span>(_ scene: <span class="text-blue-300">UIScene</span>, willConnectTo...) {
          </div>

          <div :class="[
            'p-1.5 rounded transition-all duration-300 pl-8',
            activeStep === 3 
              ? 'bg-emerald-500/20 border-l-4 border-emerald-400 text-white font-bold shadow-lg ring-1 ring-emerald-500/30' 
              : 'opacity-30'
          ]">
            window?.rootViewController = navigator.rootViewController<br/>
            navigator.route(baseURL)
          </div>

          <div :class="['transition-opacity duration-300 pl-4', activeStep ? 'opacity-40' : '']">}</div>
          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">}</div>
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

with open(f"{components_dir}/HotwireIosSetupSlide.vue", "w") as f:
    f.write(hotwire_ios)

# 4. HotwireAndroidSetupSlide.vue
hotwire_android = '''<template>
  <div class="hotwire-android-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">{{ currentLang === 'zh' ? '🤖 Android 原生整合' : '🤖 Android Integration' }}</span>
      <span class="text-xs font-mono text-slate-400">Kotlin SDK</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left flex items-center justify-between">
      <span>{{ currentLang === 'zh' ? '整合 Hotwire Native 至 Android' : 'Adding Hotwire Native to Android' }} <span class="text-emerald-400">(Kotlin) 🤖</span></span>
      
      <!-- Stepper Controls -->
      <div class="flex items-center gap-1.5 font-mono text-xs">
        <button 
          v-for="step in [1, 2, 3]" 
          :key="step"
          @click="activeStep = step"
          :class="[
            'px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold',
            activeStep === step 
              ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 shadow-lg scale-105 ring-1 ring-emerald-500/50' 
              : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'
          ]">
          {{ currentLang === 'zh' ? '步驟' : 'Step' }} {{ step }}
        </button>
      </div>
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center text-left">
      <div class="md:col-span-5 space-y-2.5">
        <div 
          @click="activeStep = 1"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 1 
              ? 'bg-slate-900 border-emerald-500/60 shadow-lg ring-1 ring-emerald-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 1 ? 'bg-emerald-500/20 text-emerald-400 border border-emerald-500/40' : 'bg-slate-800 text-slate-400']">1</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">1. {{ currentLang === 'zh' ? '加入 Gradle 依賴套件' : 'Add Gradle Dependency' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                {{ currentLang === 'zh' ? '導入 dev.hotwire:native 官方庫。' : 'Include dev.hotwire:native library.' }}
              </p>
            </div>
          </div>
        </div>

        <div 
          @click="activeStep = 2"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 2 
              ? 'bg-slate-900 border-amber-500/60 shadow-lg ring-1 ring-amber-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 2 ? 'bg-amber-500/20 text-amber-300 border border-amber-500/40' : 'bg-slate-800 text-slate-400']">2</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">2. {{ currentLang === 'zh' ? '繼承 HotwireActivity' : 'Extend HotwireActivity' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                {{ currentLang === 'zh' ? '讓 MainActivity 繼承 Hotwire 框架元件。' : 'Extend MainActivity with HotwireActivity.' }}
              </p>
            </div>
          </div>
        </div>

        <div 
          @click="activeStep = 3"
          :class="[
            'p-3 rounded-xl border transition-all cursor-pointer relative overflow-hidden',
            activeStep === 3 
              ? 'bg-slate-900 border-cyan-500/60 shadow-lg ring-1 ring-cyan-500/40 translate-x-1' 
              : 'bg-slate-900/60 border-slate-800 opacity-70 hover:opacity-100'
          ]">
          <div class="flex items-start gap-2.5">
            <span :class="['w-6 h-6 rounded-lg flex items-center justify-center font-bold text-xs shrink-0', activeStep === 3 ? 'bg-cyan-500/20 text-cyan-400 border border-cyan-500/40' : 'bg-slate-800 text-slate-400']">3</span>
            <div>
              <h4 class="text-xs font-bold text-white m-0">3. {{ currentLang === 'zh' ? '設定起始網址' : 'Define Start Location' }}</h4>
              <p class="text-[11px] text-slate-300 leading-snug m-0 mt-0.5">
                {{ currentLang === 'zh' ? '覆寫 startLocation 指向 Rails 網址。' : 'Override startLocation to Rails URL.' }}
              </p>
            </div>
          </div>
        </div>
      </div>

      <!-- Right Column: Code -->
      <div class="md:col-span-7 space-y-1.5">
        <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
          <span class="text-emerald-400 font-bold">android/app/src/main/.../MainActivity.kt</span>
          <span class="bg-slate-900 text-emerald-300 px-2 py-0.5 rounded text-[10px] border border-slate-800 font-bold">{{ currentLang === 'zh' ? '步驟' : 'Step' }} {{ activeStep }} / 3</span>
        </div>

        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto leading-relaxed space-y-1 relative">
          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">
            <span class="text-purple-400">package</span> et.netale.litloop<br/>
            <span class="text-purple-400">import</span> <span class="text-amber-300">dev.hotwire.navigation.activities.HotwireActivity</span>
          </div>

          <div :class="[
            'p-1.5 rounded transition-all duration-300',
            activeStep === 2 
              ? 'bg-amber-500/20 border-l-4 border-amber-400 text-white font-bold shadow-lg ring-1 ring-amber-500/30' 
              : 'opacity-30'
          ]">
            <span class="text-purple-400">class</span> <span class="text-emerald-300">MainActivity</span> : <span class="text-amber-300">HotwireActivity</span>() {
          </div>

          <div :class="[
            'p-1.5 rounded transition-all duration-300 pl-4',
            activeStep === 3 
              ? 'bg-cyan-500/20 border-l-4 border-cyan-400 text-white font-bold shadow-lg ring-1 ring-cyan-500/30' 
              : 'opacity-30'
          ]">
            &nbsp;&nbsp;<span class="text-purple-400">override val</span> startLocation = <span class="text-emerald-300">"https://litloop.club"</span>
          </div>

          <div :class="['transition-opacity duration-300', activeStep ? 'opacity-40' : '']">}</div>
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

with open(f"{components_dir}/HotwireAndroidSetupSlide.vue", "w") as f:
    f.write(hotwire_android)

print("Updated HotwireNativeIntroSlide, MonorepoSetupSlide, HotwireIosSetupSlide, HotwireAndroidSetupSlide")
