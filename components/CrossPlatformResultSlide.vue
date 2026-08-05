<template>
  <div class="cross-platform-result-slide w-full my-auto flex flex-col justify-center h-full overflow-hidden">
    <!-- Clean Minimalist Header -->
    <h2 class="text-xl font-black tracking-tight text-white mb-2 text-left">
      The Result: <span class="text-transparent bg-clip-text bg-gradient-to-r from-red-400 via-amber-300 to-blue-400">Web, iOS & Android Side-by-Side 📱🌐</span>
    </h2>

    <!-- 3 Column Side-by-Side Platform Showcase Grid (Maximizing Height) -->
    <div class="grid grid-cols-3 gap-3 items-stretch text-left flex-1 min-h-0">
      
      <!-- COLUMN 1: WEB BROWSER -->
      <div class="bg-slate-900/90 border border-red-500/30 rounded-xl p-2 shadow-lg flex flex-col justify-between overflow-hidden">
        <div class="font-bold text-xs text-white border-b border-slate-800 pb-1 mb-1.5 flex items-center justify-between">
          <span>🌐 Web Browser</span>
        </div>

        <!-- Screenshot Container (Maximized Vertical Space) -->
        <div class="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-1 shadow-inner flex items-center justify-center overflow-hidden min-h-[290px]">
          <img 
            v-if="hasWebImage" 
            :src="webImgSrc" 
            alt="Web Browser Result" 
            class="w-full h-full object-contain rounded"
          />
          <div v-else class="p-2 text-center space-y-0.5">
            <span class="text-xl">🌐</span>
            <div class="text-[10px] font-mono text-red-300 font-bold">Web Screenshot</div>
            <div class="text-[8px] text-slate-500 font-mono">result_web.jpg</div>
          </div>
        </div>
      </div>

      <!-- COLUMN 2: IOS NATIVE APP -->
      <div class="bg-slate-900/90 border border-blue-500/30 rounded-xl p-2 shadow-lg flex flex-col justify-between overflow-hidden">
        <div class="font-bold text-xs text-white border-b border-slate-800 pb-1 mb-1.5 flex items-center justify-between">
          <span>🍏 Native iOS</span>
        </div>

        <!-- Screenshot Container (Maximized Vertical Space) -->
        <div class="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-1 shadow-inner flex items-center justify-center overflow-hidden min-h-[290px]">
          <img 
            v-if="hasIosImage" 
            :src="iosImgSrc" 
            alt="iOS App Result" 
            class="w-full h-full object-contain rounded"
          />
          <div v-else class="p-2 text-center space-y-0.5">
            <span class="text-xl">🍏</span>
            <div class="text-[10px] font-mono text-blue-300 font-bold">iOS Screenshot</div>
            <div class="text-[8px] text-slate-500 font-mono">result_ios.jpg</div>
          </div>
        </div>
      </div>

      <!-- COLUMN 3: ANDROID NATIVE APP -->
      <div class="bg-slate-900/90 border border-emerald-500/30 rounded-xl p-2 shadow-lg flex flex-col justify-between overflow-hidden">
        <div class="font-bold text-xs text-white border-b border-slate-800 pb-1 mb-1.5 flex items-center justify-between">
          <span>🤖 Native Android</span>
        </div>

        <!-- Screenshot Container (Maximized Vertical Space) -->
        <div class="flex-1 bg-slate-950 border border-slate-800 rounded-lg p-1 shadow-inner flex items-center justify-center overflow-hidden min-h-[290px]">
          <img 
            v-if="hasAndroidImage" 
            :src="androidImgSrc" 
            alt="Android App Result" 
            class="w-full h-full object-contain rounded"
          />
          <div v-else class="p-2 text-center space-y-0.5">
            <span class="text-xl">🤖</span>
            <div class="text-[10px] font-mono text-emerald-300 font-bold">Android Screenshot</div>
            <div class="text-[8px] text-slate-500 font-mono">result_android.jpg</div>
          </div>
        </div>
      </div>

    </div>

  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const webImgSrc = ref('/result_web.jpg')
const iosImgSrc = ref('/result_ios.jpg')
const androidImgSrc = ref('/result_android.jpg')

const hasWebImage = ref(false)
const hasIosImage = ref(false)
const hasAndroidImage = ref(false)

const checkImage = (url, refVar) => {
  const img = new Image()
  img.onload = () => { refVar.value = true }
  img.onerror = () => { refVar.value = false }
  img.src = url
}

onMounted(() => {
  checkImage(webImgSrc.value, hasWebImage)
  checkImage(iosImgSrc.value, hasIosImage)
  checkImage(androidImgSrc.value, hasAndroidImage)
})
</script>
