# Vite SCSS Compilation and Minification Setup

This guide explains how to integrate Vite for SCSS compilation and CSS minification in a Flask project. It covers installation, configuration, and usage.

## Installation
Ensure you have **Node.js** installed. Then, install the required dependencies:

```sh
npm install vite sass autoprefixer cssnano --save-dev
```


## Configuration

### `package.json`

```json
{
  "name": "flask-datta-able",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "dev": "vite build --watch --mode development",
    "build": "vite build --mode production && npm run minify-css",
    "minify-css": "cssnano static/assets/css/*.css --dir static/assets/css --no-map --suffix .min"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "devDependencies": {
    "autoprefixer": "^10.4.20",
    "cssnano": "^7.0.6",
    "sass": "^1.85.1",
    "vite": "^6.2.0"
  }
}
```

### `vite.config.js`

```javascript
import { defineConfig } from "vite";
import autoprefixer from "autoprefixer";
import cssnano from "cssnano";
import path from "path";

export default defineConfig(({ mode }) => {
    const isProduction = mode === "production";

    return {
        css: {
            postcss: {
                plugins: [
                    autoprefixer(),
                    isProduction && cssnano(),
                ].filter(Boolean),
            },
        },
        build: {
            outDir: "static",
            emptyOutDir: false,
            rollupOptions: {
                input: path.resolve(__dirname, "static/assets/scss/custom.scss"),
                output: {
                    assetFileNames: (assetInfo) => {
                        if (assetInfo.name === "custom.css") {
                            return "assets/css/custom.css";
                        }
                        return "assets/css/[name].[ext]";
                    },
                },
            },
        },
    };
});
```

## Usage

### **Development Mode (Auto-Compile on Changes)**

```sh
npm run dev
```

### **Production Build (Minify CSS & Compile SCSS)**

```sh
npm run build
```