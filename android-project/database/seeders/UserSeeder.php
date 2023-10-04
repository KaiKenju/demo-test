<?php

namespace Database\Seeders;

use Illuminate\Database\Console\Seeds\WithoutModelEvents;
use Illuminate\Database\Seeder;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        // Create admin user
        \App\Models\User::factory()->create([
            'name' => 'hiepman',
            'first_name' => 'Hiep',
            'last_name' => 'Man',
            'email' => 'hiepdv.tb288@gmail.com',
            'password' => bcrypt('123456'),
            'avatar' => '',
        ]);
    }
}
