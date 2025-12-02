import react from '@vitejs/plugin-react';
import laravel from 'laravel-vite-plugin';
import {
    defineConfig
} from 'vite';
import tailwindcss from "@tailwindcss/vite";

export default defineConfig({
    plugins: [
        laravel({
            input: ['resources/css/app.css', 'resources/js/app.tsx'],
            ssr: 'resources/js/ssr.jsx',
            refresh: true,
        }),
        react(),
        tailwindcss(),
    ],
    esbuild: {
        jsx: 'automatic',
    },
    server: {
        // 1. host: '0.0.0.0' : 컨테이너 내부에서 모든 인터페이스에 바인딩 (외부 연결 허용)
        // host: '0.0.0.0', 
        // port: 5173,
        // 2. hmr 설정을 추가하여 브라우저에게 전달할 주소를 명시합니다.
        hmr: {
            // 브라우저가 접속해야 할 주소는 호스트 PC의 localhost입니다.
            host: 'localhost', 
            port: 5173,
            clientPort: 5173,
            protocol: 'ws',
        }
    }
});