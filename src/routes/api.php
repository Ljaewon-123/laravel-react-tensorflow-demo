<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\SentimentController;

Route::middleware('auth')->group(function () {
  Route::post('/sentiment', [SentimentController::class, 'detect'])->name('detect');
})