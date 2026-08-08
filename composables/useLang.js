import { ref } from 'vue'

export const currentLang = ref('en')

export function setLang(lang) {
  currentLang.value = lang
}
