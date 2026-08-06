<template>
  <div class="monorepo-setup-slide w-full my-auto flex flex-col justify-center">
    <!-- Header -->
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">📁 LitLoop Monorepo</span>
      <span class="text-xs font-mono text-slate-400">https://litloop.club</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left flex items-center justify-between">
      <span>Monorepo Setup: <span class="text-red-500">Rails + iOS + Android 📦</span></span>
      
      <!-- Project Tab Selector Buttons -->
      <div class="flex items-center gap-1.5 font-mono text-xs">
        <button 
          @click="activeTab = 'backend'"
          :class="['px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold', activeTab === 'backend' ? 'bg-red-950/80 border-red-500 text-red-300 shadow-lg scale-105' : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white']">
          💎 Backend
        </button>

        <button 
          @click="activeTab = 'ios'"
          :class="['px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold', activeTab === 'ios' ? 'bg-blue-950/80 border-blue-500 text-blue-300 shadow-lg scale-105' : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white']">
          🍏 iOS
        </button>

        <button 
          @click="activeTab = 'android'"
          :class="['px-2.5 py-1 rounded-lg border transition-all flex items-center gap-1 font-bold', activeTab === 'android' ? 'bg-emerald-950/80 border-emerald-500 text-emerald-300 shadow-lg scale-105' : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white']">
          🤖 Android
        </button>
      </div>
    </h2>

    <!-- 2 Column Grid Layout: Left Root Monorepo Tree, Right Detailed Project Structure & Code -->
    <div class="grid grid-cols-1 md:grid-cols-12 gap-4 items-center">
      
      <!-- Left Column: Monorepo Root Directory Tree (Cols 1-5) -->
      <div class="md:col-span-5 text-left">
        <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-xs text-slate-300 space-y-2">
          <div class="flex items-center justify-between border-b border-slate-800 pb-2 text-[11px] text-slate-400">
            <span class="flex items-center gap-1.5 text-white font-bold">
              <span class="w-2.5 h-2.5 rounded-full bg-emerald-500 animate-pulse"></span>
              arif-nibaboch/
            </span>
            <span class="text-[10px] bg-slate-900 px-2 py-0.5 rounded text-amber-300">Root Directory</span>
          </div>

          <!-- Directory Tree Folders -->
          <div class="space-y-2 text-[11px]">
            
            <!-- Backend Folder Item -->
            <div 
              @click="activeTab = 'backend'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'backend' 
                  ? 'bg-red-950/50 border-red-500 ring-1 ring-red-500/50 shadow-lg translate-x-1' 
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100'
              ]">
              <div class="text-red-400 font-bold flex items-center gap-1.5">
                <span>💎 backend/</span>
              </div>
              <span class="text-[9px] bg-red-900/60 px-1.5 py-0.5 rounded text-red-200 font-mono">Rails App</span>
            </div>

            <!-- iOS Folder Item -->
            <div 
              @click="activeTab = 'ios'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'ios' 
                  ? 'bg-blue-950/50 border-blue-500 ring-1 ring-blue-500/50 shadow-lg translate-x-1' 
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100'
              ]">
              <div class="text-blue-400 font-bold flex items-center gap-1.5">
                <span>🍏 ios/</span>
              </div>
              <span class="text-[9px] bg-blue-900/60 px-1.5 py-0.5 rounded text-blue-200 font-mono">Swift App</span>
            </div>

            <!-- Android Folder Item -->
            <div 
              @click="activeTab = 'android'"
              :class="[
                'p-2 rounded border transition-all cursor-pointer flex items-center justify-between',
                activeTab === 'android' 
                  ? 'bg-emerald-950/50 border-emerald-500 ring-1 ring-emerald-500/50 shadow-lg translate-x-1' 
                  : 'bg-slate-900/60 border-slate-800/80 opacity-70 hover:opacity-100'
              ]">
              <div class="text-emerald-400 font-bold flex items-center gap-1.5">
                <span>🤖 android/</span>
              </div>
              <span class="text-[9px] bg-emerald-900/60 px-1.5 py-0.5 rounded text-emerald-200 font-mono">Kotlin App</span>
            </div>

          </div>
        </div>
      </div>

      <!-- Right Column: Project Structure Details & Key Code (Cols 6-12) -->
      <div class="md:col-span-7 text-left space-y-1.5">
        
        <!-- BACKEND STRUCTURE TAB -->
        <div v-if="activeTab === 'backend'" class="space-y-1.5 animate-fade-in">
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
            <span class="text-red-400 font-bold">backend/ — Rails Monolith Structure</span>
            <span class="bg-red-950 text-red-300 px-2 py-0.5 rounded text-[10px] border border-red-800 font-bold">Rails 8</span>
          </div>

          <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto h-[240px] flex flex-col justify-between">
            <div class="space-y-1 text-slate-300">
              <div class="text-red-400 font-bold">backend/</div>
              <div class="pl-3 text-slate-400">├── app/</div>
              <div class="pl-6 text-slate-400">├── controllers/</div>
              <div class="pl-9 text-amber-300 font-bold bg-amber-950/60 px-1.5 py-0.5 rounded border border-amber-800/60 inline-block">
                └── configurations_controller.rb ⚡ (Serves Path Config JSON)
              </div>
              <div class="pl-6 text-slate-400">└── views/ (Renders HTML for Web & Mobile)</div>
              <div class="pl-3 text-slate-400">├── config/routes.rb</div>
              <div class="pl-3 text-slate-400">└── Gemfile</div>
            </div>

            <div class="p-2 bg-slate-900 border border-slate-800 rounded text-[10px] text-amber-300">
              <code>get "/configurations/ios_v1", to: "configurations#ios_v1"</code>
            </div>
          </div>
        </div>

        <!-- IOS STRUCTURE TAB -->
        <div v-if="activeTab === 'ios'" class="space-y-1.5 animate-fade-in">
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
            <span class="text-blue-400 font-bold">ios/ — Swift Xcode Project Structure</span>
            <span class="bg-blue-950 text-blue-300 px-2 py-0.5 rounded text-[10px] border border-blue-800 font-bold">iOS / Swift</span>
          </div>

          <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto h-[240px] flex flex-col justify-between">
            <div class="space-y-1 text-slate-300">
              <div class="text-blue-400 font-bold">ios/</div>
              <div class="pl-3 text-slate-400">├── LitLoop.xcodeproj</div>
              <div class="pl-3 text-slate-400">└── App/</div>
              <div class="pl-6 text-slate-400">├── Delegates/</div>
              <div class="pl-9 text-blue-300 font-bold bg-blue-950/60 px-1.5 py-0.5 rounded border border-blue-800/60 inline-block">
                ├── SceneDelegate.swift ⚡ (Hotwire Navigator Entry)
                <div>└── AppDelegate.swift</div>
              </div>
              <div class="pl-6 text-slate-400">└── Resources/</div>
              <div class="pl-9 text-slate-400">└── path_configuration.json</div>
            </div>

            <div class="p-2 bg-slate-900 border border-slate-800 rounded text-[10px] text-blue-300">
              <code>Navigator(configuration: .init(name: "main", startLocation: baseURL))</code>
            </div>
          </div>
        </div>

        <!-- ANDROID STRUCTURE TAB -->
        <div v-if="activeTab === 'android'" class="space-y-1.5 animate-fade-in">
          <div class="flex items-center justify-between text-[11px] font-mono text-slate-400 px-1">
            <span class="text-emerald-400 font-bold">android/ — Kotlin Gradle Project Structure</span>
            <span class="bg-emerald-950 text-emerald-300 px-2 py-0.5 rounded text-[10px] border border-emerald-800 font-bold">Android / Kotlin</span>
          </div>

          <div class="bg-slate-950 border border-slate-800 rounded-xl p-3.5 shadow-2xl font-mono text-[11px] text-slate-300 overflow-x-auto h-[240px] flex flex-col justify-between">
            <div class="space-y-1 text-slate-300">
              <div class="text-emerald-400 font-bold">android/</div>
              <div class="pl-3 text-slate-400">├── build.gradle.kts</div>
              <div class="pl-3 text-slate-400">└── app/</div>
              <div class="pl-6 text-slate-400">├── build.gradle.kts (dep: dev.hotwire:native)</div>
              <div class="pl-6 text-slate-400">└── src/main/java/et/netale/litloop/</div>
              <div class="pl-9 text-emerald-300 font-bold bg-emerald-950/60 px-1.5 py-0.5 rounded border border-emerald-800/60 inline-block">
                └── MainActivity.kt ⚡ (HotwireActivity subclass)
              </div>
            </div>

            <div class="p-2 bg-slate-900 border border-slate-800 rounded text-[10px] text-emerald-300">
              <code>class MainActivity : HotwireActivity() // startLocation = "https://litloop.club"</code>
            </div>
          </div>
        </div>

      </div>

    </div>

    <!-- Bottom Dynamic Takeaway Banner -->
    <div class="mt-3 p-2.5 bg-slate-950 border border-slate-800 rounded-xl text-left flex items-center justify-between text-xs">
      <span class="text-slate-300">
        <template v-if="activeTab === 'backend'">
          💎 <strong>Rails Backend:</strong> Houses models, controllers & ERB views + serves dynamic navigation rules for mobile.
        </template>
        <template v-if="activeTab === 'ios'">
          🍏 <strong>iOS Project:</strong> Xcode project inside <code class="text-blue-300">/ios</code> folder with Swift <code class="text-blue-300">SceneDelegate</code> entry.
        </template>
        <template v-if="activeTab === 'android'">
          🤖 <strong>Android Project:</strong> Gradle project inside <code class="text-emerald-300">/android</code> folder extending <code class="text-emerald-300">HotwireActivity</code>.
        </template>
      </span>

      <span :class="['text-[10px] font-mono px-2 py-0.5 rounded border shrink-0 font-bold ml-2', activeTab === 'backend' ? 'bg-red-950 text-red-300 border-red-700' : activeTab === 'ios' ? 'bg-blue-950 text-blue-300 border-blue-700' : 'bg-emerald-950 text-emerald-300 border-emerald-700']">
        LitLoop {{ activeTab.toUpperCase() }} ⚡
      </span>
    </div>

  </div>
</template>

<script setup>
import { ref } from 'vue'

const activeTab = ref('backend')
</script>

<style scoped>
@keyframes fadeIn {
  from { opacity: 0; transform: translateY(4px); }
  to { opacity: 1; transform: translateY(0); }
}

.animate-fade-in {
  animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
}
</style>
