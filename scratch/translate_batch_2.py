import os

components_dir = "/home/netale/coscup-hotwire-native-talk/components"

# 1. CrossPlatformResultSlide.vue
cross_platform = '''<template>
  <div class="cross-platform-result-slide w-full my-auto flex flex-col justify-center">
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">{{ currentLang === 'zh' ? '✨ 成果展示' : '✨ The Result' }}</span>
      <span class="text-xs font-mono text-slate-400">One Codebase, Three Platforms</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left">
      {{ currentLang === 'zh' ? '一套 Rails Codebase 發佈三端 App 🚀' : 'One Rails Codebase. Three Platforms. 🚀' }}
    </h2>

    <!-- Platform Mockup Selector Tabs -->
    <div class="flex items-center gap-2 mb-3">
      <button 
        v-for="platform in ['all', 'ios', 'android', 'web']" 
        :key="platform"
        @click="selectedPlatform = platform"
        :class="[
          'px-3 py-1 rounded-lg font-mono text-xs font-bold transition-all border',
          selectedPlatform === platform
            ? 'bg-red-950 border-red-500 text-red-300 shadow-lg scale-105'
            : 'bg-slate-900 border-slate-800 text-slate-400 hover:text-white'
        ]">
        <template v-if="platform === 'all'">{{ currentLang === 'zh' ? '📱 廣角全視角' : '📱 All 3 Platforms' }}</template>
        <template v-if="platform === 'ios'">🍏 iOS App</template>
        <template v-if="platform === 'android'">🤖 Android App</template>
        <template v-if="platform === 'web'">🌐 Web Browser</template>
      </button>
    </div>

    <!-- 3 Platforms Visual Preview Grid -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 my-2">
      <div 
        v-show="selectedPlatform === 'all' || selectedPlatform === 'ios'"
        class="bg-slate-900/90 border border-blue-500/40 rounded-2xl p-3 shadow-xl space-y-2 text-left">
        <div class="flex justify-between items-center border-b border-slate-800 pb-1.5">
          <span class="text-xs font-bold text-blue-400 flex items-center gap-1">🍏 iOS Native</span>
          <span class="text-[10px] font-mono text-slate-400">Swift Shell</span>
        </div>
        <p class="text-[11px] text-slate-300 m-0">
          {{ currentLang === 'zh' ? '原生 iOS NavigationBar 與順暢滑動體驗。' : 'Native navigation bar, smooth touch feedback & gesture back.' }}
        </p>
      </div>

      <div 
        v-show="selectedPlatform === 'all' || selectedPlatform === 'android'"
        class="bg-slate-900/90 border border-emerald-500/40 rounded-2xl p-3 shadow-xl space-y-2 text-left">
        <div class="flex justify-between items-center border-b border-slate-800 pb-1.5">
          <span class="text-xs font-bold text-emerald-400 flex items-center gap-1">🤖 Android Native</span>
          <span class="text-[10px] font-mono text-slate-400">Kotlin Shell</span>
        </div>
        <p class="text-[11px] text-slate-300 m-0">
          {{ currentLang === 'zh' ? '原生 TopAppBar 與 Android 原生微互動。' : 'Native TopAppBar, material ripple effects & back stack.' }}
        </p>
      </div>

      <div 
        v-show="selectedPlatform === 'all' || selectedPlatform === 'web'"
        class="bg-slate-900/90 border border-red-500/40 rounded-2xl p-3 shadow-xl space-y-2 text-left">
        <div class="flex justify-between items-center border-b border-slate-800 pb-1.5">
          <span class="text-xs font-bold text-red-400 flex items-center gap-1">🌐 Web Browser</span>
          <span class="text-[10px] font-mono text-slate-400">Turbo Drive</span>
        </div>
        <p class="text-[11px] text-slate-300 m-0">
          {{ currentLang === 'zh' ? '桌上型電腦與行動網頁使用相同的 ERB 視圖。' : 'Desktop & Mobile web app using exact same ERB views.' }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { currentLang } from '../composables/useLang'

const selectedPlatform = ref('all')
</script>
'''

with open(f"{components_dir}/CrossPlatformResultSlide.vue", "w") as f:
    f.write(cross_platform)

# 2. HotwireDetectionSlide.vue
hotwire_detection = '''<template>
  <div class="hotwire-detection-slide w-full my-auto flex flex-col justify-center">
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">{{ currentLang === 'zh' ? '🔍 裝置識別' : '🔍 Client Detection' }}</span>
      <span class="text-xs font-mono text-slate-400">User-Agent Request Header</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left">
      {{ currentLang === 'zh' ? 'Rails 如何識別是原生 App 請求？' : 'How Rails Knows It\'s Hotwire Native 📱' }}
    </h2>

    <div class="bg-slate-900/90 border border-slate-800 rounded-2xl p-4 text-left shadow-xl space-y-3">
      <p class="text-xs text-slate-300 leading-relaxed m-0">
        {{ currentLang === 'zh'
          ? 'Hotwire Native 會自動在 HTTP 請求標頭 (User-Agent) 中附帶 Hotwire-Native 標記！'
          : 'Hotwire Native app automatically appends a custom User-Agent string to every request.' }}
      </p>

      <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 font-mono text-xs text-slate-200">
        <div class="text-amber-400 mb-1"># app/controllers/application_controller.rb</div>
        <div><span class="text-purple-400">include</span> Hotwire::Native::Navigation</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/HotwireDetectionSlide.vue", "w") as f:
    f.write(hotwire_detection)

# 3. TailwindNativeHidingSlide.vue
tailwind_native = '''<template>
  <div class="tailwind-native-hiding-slide w-full my-auto flex flex-col justify-center">
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">{{ currentLang === 'zh' ? '🎨 UI 條件式顯示' : '🎨 Conditional UI' }}</span>
      <span class="text-xs font-mono text-slate-400">Tailwind & CSS Helper</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left">
      {{ currentLang === 'zh' ? '使用 CSS 隱藏或顯示原生專屬元件 🙈' : 'Hiding Elements in Native Views 🙈' }}
    </h2>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-slate-200 text-left space-y-2">
      <div class="text-slate-400">
        {{ currentLang === 'zh' ? '當在 Native App 容器中打開時，隱藏重複的 Web 導覽列：' : 'Hide redundant web navbar when rendered inside native app:' }}
      </div>
      <div class="p-2 bg-slate-900 border border-slate-800 rounded text-emerald-300">
        <code>&lt;nav class="hotwire-native:hidden"&gt;...&lt;/nav&gt;</code>
      </div>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/TailwindNativeHidingSlide.vue", "w") as f:
    f.write(tailwind_native)

# 4. DynamicNativeTitleSlide.vue
dynamic_title = '''<template>
  <div class="dynamic-native-title-slide w-full my-auto flex flex-col justify-center">
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">{{ currentLang === 'zh' ? '🏷️ 標題同步' : '🏷️ Dynamic Title' }}</span>
      <span class="text-xs font-mono text-slate-400">HTML Title Sync</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-2 text-left">
      {{ currentLang === 'zh' ? '自動將原生 NavigationBar 標題同步 ⚡' : 'Dynamic Native Header Title ⚡' }}
    </h2>

    <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 font-mono text-xs text-slate-200 text-left space-y-2">
      <div class="text-slate-400">
        {{ currentLang === 'zh' ? '只需在 HTML 設定 `<title>`，Hotwire Native 就會自動更新手機端標題：' : 'Just set standard HTML `<title>`, Hotwire Native updates native navigation title:' }}
      </div>
      <div class="p-2 bg-slate-900 border border-slate-800 rounded text-amber-300">
        <code>&lt;% provide(:title, "Book Details") %&gt;</code>
      </div>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/DynamicNativeTitleSlide.vue", "w") as f:
    f.write(dynamic_title)

# 5. LiveDemoSlide.vue
live_demo = '''<template>
  <div class="live-demo-slide w-full my-auto flex flex-col justify-center text-center">
    <div class="mb-3">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '🎬 實機展示' : '🎬 Live Demonstration' }}</span>
    </div>

    <h2 class="text-4xl font-black tracking-tight text-white mb-3">
      <template v-if="currentLang === 'zh'">
        現場實機展示：<span class="text-red-500">LitLoop App 📱</span>
      </template>
      <template v-else>
        Live Demo: <span class="text-red-500">LitLoop App 📱</span>
      </template>
    </h2>

    <p class="text-slate-300 text-sm max-w-lg mx-auto">
      {{ currentLang === 'zh' ? '直擊 Rails, iOS 與 Android 原生流暢體驗！' : 'Witness seamless Rails, iOS, and Android native bridge in action!' }}
    </p>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/LiveDemoSlide.vue", "w") as f:
    f.write(live_demo)

# 6. WhatElseHotwireNativeSlide.vue
what_else = '''<template>
  <div class="what-else-slide w-full my-auto flex flex-col justify-center text-left">
    <div class="flex justify-between items-center mb-1">
      <span class="hotwire-badge font-bold">{{ currentLang === 'zh' ? '⚡ 進階功能' : '⚡ Advanced Capabilities' }}</span>
      <span class="text-xs font-mono text-slate-400">Strada & Bridge Components</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-4">
      {{ currentLang === 'zh' ? 'Hotwire Native 還支援哪些原生功能？ 📱' : 'What Else Can Hotwire Native Do? 📱' }}
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-3 gap-4 mb-4">
      <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow-xl space-y-2">
        <span class="text-2xl">🌉</span>
        <h3 class="text-sm font-bold text-white m-0">Strada Components</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '將 Web HTML 按鈕與原生 iOS/Android 按鈕綁定與通訊。' : 'Bridge Web HTML elements to native iOS/Android component controls.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow-xl space-y-2">
        <span class="text-2xl">🔔</span>
        <h3 class="text-sm font-bold text-white m-0">Push Notifications</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '完全支援 APNs 與 FCM，一按直接開啟原生頁面。' : 'Full APNs & FCM support with deep linking into server paths.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-slate-800 rounded-xl p-4 shadow-xl space-y-2">
        <span class="text-2xl">📷</span>
        <h3 class="text-sm font-bold text-white m-0">Hardware Access</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '調用相機、生物辨識 FaceID/TouchID 與定位權限。' : 'Access camera, biometric FaceID/TouchID, and geolocation.' }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/WhatElseHotwireNativeSlide.vue", "w") as f:
    f.write(what_else)

# 7. WhenNotToUseHotwireNativeSlide.vue
when_not = '''<template>
  <div class="when-not-to-use-slide w-full my-auto flex flex-col justify-center text-left">
    <div class="flex justify-between items-center mb-1">
      <span class="rails-badge font-bold">{{ currentLang === 'zh' ? '⚖️ 客觀評估' : '⚖️ Objective Tradeoffs' }}</span>
      <span class="text-xs font-mono text-slate-400">When NOT To Use</span>
    </div>

    <h2 class="text-2xl font-black tracking-tight text-white mb-4">
      {{ currentLang === 'zh' ? '什麼時候不適合使用 Hotwire Native？ 🚫' : 'When NOT To Use Hotwire Native 🚫' }}
    </h2>

    <div class="grid grid-cols-1 md:grid-cols-2 gap-4 mb-4">
      <div class="bg-slate-900/90 border border-red-500/30 rounded-xl p-4 shadow-xl space-y-2">
        <h3 class="text-sm font-bold text-red-400 m-0 flex items-center gap-1">🎮 {{ currentLang === 'zh' ? '高度依賴離線 3D/遊戲' : 'Offline Heavy 3D / Games' }}</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '複雜 3D 遊戲或完全無網路完全離線編輯的硬核工具。' : 'High-fps 3D games or completely offline graphic editing tools.' }}
        </p>
      </div>

      <div class="bg-slate-900/90 border border-amber-500/30 rounded-xl p-4 shadow-xl space-y-2">
        <h3 class="text-sm font-bold text-amber-400 m-0 flex items-center gap-1">🔌 {{ currentLang === 'zh' ? '無 Web 端的純獨立硬體工具' : 'No Web Companion' }}</h3>
        <p class="text-xs text-slate-300 m-0">
          {{ currentLang === 'zh' ? '沒有任何 Web 端，全靠藍芽/硬體溝通的專用工具。' : 'Standalone Bluetooth apps that have no web app component.' }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { currentLang } from '../composables/useLang'
</script>
'''

with open(f"{components_dir}/WhenNotToUseHotwireNativeSlide.vue", "w") as f:
    f.write(when_not)

print("Updated CrossPlatformResultSlide, HotwireDetectionSlide, TailwindNativeHidingSlide, DynamicNativeTitleSlide, LiveDemoSlide, WhatElseHotwireNativeSlide, WhenNotToUseHotwireNativeSlide")
