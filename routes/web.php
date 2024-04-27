<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider and all of them will
| be assigned to the "web" middleware group. Make something great!
|
 */

Route::domain('{user_name}.vyaparapp.test')->group(function () {
    Route::get('/', function ($user_name) {
        return "Hello $user_name!";
    });
});

Route::get('/test', function () {
    return 'Test Route';
});
