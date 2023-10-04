<?php

namespace App\Models;

use Illuminate\Database\Eloquent\Concerns\HasTimestamps;
use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class Repo extends Model
{
    use HasFactory, HasTimestamps;
    protected $table = 'repos';
    protected $fillable = [
        'name',
        'readme',
        'language',
        'created_by',
        'mode',
    ];
}
