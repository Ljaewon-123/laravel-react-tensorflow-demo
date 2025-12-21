<?php

use Illuminate\Support\Facades\Route;
use App\Http\Controllers\SentimentController;


Route::post('/ping', function () {
    return response()->json(['pong' => true]);
});


Route::middleware('auth')->group(function () {
  Route::post('/sentiment', [SentimentController::class, 'detect'])->name('detect');
});

Route::post('/sentiment/test', [SentimentController::class, 'detect']);
