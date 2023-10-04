<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class LoginController extends Controller
{
    public function index(Request $request)
    {
        $loginData = [
            'name' => $request->get('name'),
            'password' => $request->get('password'),
        ];
        if (Auth::attempt($loginData)) {
            $user = Auth::user();
            return response()->json([
                'status' => 200,
                'message' => 'Successfully login',
                'data' => $user,
            ]);
        } else {
            return response()->json([
                'status' => 417,
                'message' => 'User not found',
            ]);
        }
    }
}
