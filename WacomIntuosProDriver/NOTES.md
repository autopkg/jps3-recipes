*Taken from binary 'Wacom Tablet Utility'*



```

void -[OMainViewController uninstall:](void * self, void * _cmd, void * arg2) {
    [self->mProgressIndicator setHidden:0x0];
    [self->mProgressIndicator startAnimation:self];
    [self shutDownOthers:0x0];
    var_40 = @"BundleID";
    var_38 = @"com.wacom.wacomtablet";
    rdx = [NSDictionary dictionaryWithObjects:0x0 forKeys:rcx count:0x1];
    [self->mUpdaterClient stopProcess:rdx];
    var_50 = @"BundleID";
    var_48 = @"com.wacom.wacomtablet";
    [self->mUpdaterClient stopProcess:[NSDictionary dictionaryWithObjects:rdx forKeys:rcx count:0x1]];
    rbx = [OPersistentDataStoreClient client];
    [rbx connectToService];
    [rbx stopService];
    r14 = [[NSTask alloc] init];
    rbx = [NSMutableArray array];
    [rbx addObject:@"unload"];
    [rbx addObject:@"/Library/LaunchAgents/com.wacom.wacomtablet.plist"];
    [r14 setLaunchPath:@"/bin/launchctl"];
    [r14 setArguments:rbx];
    [r14 launch];
    [r14 waitUntilExit];
    r14 = [[NSTask alloc] init];
    rbx = [NSMutableArray array];
    [rbx addObject:@"unload"];
    [rbx addObject:@"/Library/LaunchAgents/com.wacom.DataStoreMgr.plist"];
    [r14 setLaunchPath:@"/bin/launchctl"];
    [r14 setArguments:rbx];
    [r14 launch];
    [r14 waitUntilExit];
    var_60 = @"Domain";
    var_58 = @"User";
    rdx = [NSDictionary dictionaryWithObjects:rbx forKeys:rcx count:0x1];
    [self->mUpdaterClient removePrefs:rdx];
    var_70 = @"Default";
    var_80 = intrinsic_movdqa(var_80, intrinsic_punpcklqdq(zero_extend_64(@"Professional"), zero_extend_64(@"Common")));
    var_68 = [NSArray arrayWithObjects:rdx count:0x2];
    [self->mUpdaterClient performRemove:[NSDictionary dictionaryWithObjects:rdx forKeys:&var_70 count:0x1]];
    [self->mUpdaterClient stopService];
    [self->mProgressIndicator stopAnimation:self];
    [self->mProgressIndicator setHidden:0x1];
    if (*___stack_chk_guard != *___stack_chk_guard) {
            __stack_chk_fail();
    }
    return;
}

/* */


void * -[OUpdaterClient stopProcess:](void * self, void * _cmd, void * arg2) {
    var_68 = 0x0;
    *(&var_68 + 0x8) = &var_68;
    *(int32_t *)(&var_68 + 0x10) = 0x52000000;
    *(int32_t *)(&var_68 + 0x14) = 0x30;
    xmm0 = zero_extend_64(___Block_byref_object_dispose_);
    *(int128_t *)(&var_68 + 0x18) = intrinsic_movdqu(*(int128_t *)(&var_68 + 0x18), intrinsic_punpcklqdq(zero_extend_64(___Block_byref_object_copy_), xmm0, arg2, ___Block_byref_object_copy_));
    *(&var_68 + 0x28) = 0x0;
    var_38 = 0x0;
    *(&var_38 + 0x8) = &var_38;
    *(int32_t *)(&var_38 + 0x10) = 0x20000000;
    *(int32_t *)(&var_38 + 0x14) = 0x20;
    *(int8_t *)(&var_38 + 0x18) = 0x0;
    var_98 = __NSConcreteStackBlock;
    *(int32_t *)(&var_98 + 0x8) = 0xc2000000;
    *(int32_t *)(&var_98 + 0xc) = 0x0;
    *(&var_98 + 0x10) = ___30-[OUpdaterClient stopProcess:]_block_invoke;
    *(&var_98 + 0x18) = ___block_descriptor_tmp.50;
    *(&var_98 + 0x20) = &var_68;
    *(&var_98 + 0x28) = &var_38;
    [self->mRemoteProxy stopProcess:rdx withReply:rcx];
    rbx = 0x65;
    do {
            if (*(int8_t *)(var_30 + 0x18) != 0x0) {
                break;
            }
            xmm0 = intrinsic_movsd(xmm0, *0x10007b730);
            [NSThread sleepForTimeInterval:rdx];
            rbx = rbx - 0x1;
    } while (rbx >= 0x2);
    _Block_object_dispose(&var_38, 0x8);
    _Block_object_dispose(&var_68, 0x8);
    rax = *(*(&var_68 + 0x8) + 0x28);
    return rax;
}

/* */

void * -[OUpdaterClient removePrefs:](void * self, void * _cmd, void * arg2) {
    var_68 = 0x0;
    *(&var_68 + 0x8) = &var_68;
    *(int32_t *)(&var_68 + 0x10) = 0x52000000;
    *(int32_t *)(&var_68 + 0x14) = 0x30;
    xmm0 = zero_extend_64(___Block_byref_object_dispose_);
    *(int128_t *)(&var_68 + 0x18) = intrinsic_movdqu(*(int128_t *)(&var_68 + 0x18), intrinsic_punpcklqdq(zero_extend_64(___Block_byref_object_copy_), xmm0, arg2, ___Block_byref_object_copy_));
    *(&var_68 + 0x28) = 0x0;
    var_38 = 0x0;
    *(&var_38 + 0x8) = &var_38;
    *(int32_t *)(&var_38 + 0x10) = 0x20000000;
    *(int32_t *)(&var_38 + 0x14) = 0x20;
    *(int8_t *)(&var_38 + 0x18) = 0x0;
    var_98 = __NSConcreteStackBlock;
    *(int32_t *)(&var_98 + 0x8) = 0xc2000000;
    *(int32_t *)(&var_98 + 0xc) = 0x0;
    *(&var_98 + 0x10) = ___30-[OUpdaterClient removePrefs:]_block_invoke;
    *(&var_98 + 0x18) = ___block_descriptor_tmp.34;
    *(&var_98 + 0x20) = &var_68;
    *(&var_98 + 0x28) = &var_38;
    [self->mRemoteProxy removePrefs:rdx withReply:rcx];
    rbx = 0x65;
    do {
            if (*(int8_t *)(var_30 + 0x18) != 0x0) {
                break;
            }
            xmm0 = intrinsic_movsd(xmm0, *0x10007b730);
            [NSThread sleepForTimeInterval:rdx];
            rbx = rbx - 0x1;
    } while (rbx >= 0x2);
    _Block_object_dispose(&var_38, 0x8);
    _Block_object_dispose(&var_68, 0x8);
    rax = *(*(&var_68 + 0x8) + 0x28);
    return rax;
}

/* */

void * -[OUpdaterClient performRemove:](void * self, void * _cmd, void * arg2) {
    var_38 = 0x0;
    *(&var_38 + 0x8) = &var_38;
    *(int32_t *)(&var_38 + 0x10) = 0x20000000;
    *(int32_t *)(&var_38 + 0x14) = 0x20;
    *(int8_t *)(&var_38 + 0x18) = 0x0;
    var_68 = 0x0;
    *(&var_68 + 0x8) = &var_68;
    *(int32_t *)(&var_68 + 0x10) = 0x52000000;
    *(int32_t *)(&var_68 + 0x14) = 0x30;
    xmm0 = zero_extend_64(___Block_byref_object_dispose_);
    *(int128_t *)(&var_68 + 0x18) = intrinsic_movdqu(*(int128_t *)(&var_68 + 0x18), intrinsic_punpcklqdq(zero_extend_64(___Block_byref_object_copy_), xmm0, arg2, ___Block_byref_object_copy_));
    *(&var_68 + 0x28) = 0x0;
    var_98 = __NSConcreteStackBlock;
    *(int32_t *)(&var_98 + 0x8) = 0xc2000000;
    *(int32_t *)(&var_98 + 0xc) = 0x0;
    *(&var_98 + 0x10) = ___32-[OUpdaterClient performRemove:]_block_invoke;
    *(&var_98 + 0x18) = ___block_descriptor_tmp.30;
    *(&var_98 + 0x20) = &var_68;
    *(&var_98 + 0x28) = &var_38;
    [self->mRemoteProxy performRemove:rdx withReply:rcx];
    rbx = 0x65;
    do {
            if (*(int8_t *)(var_30 + 0x18) != 0x0) {
                break;
            }
            xmm0 = intrinsic_movsd(xmm0, *0x10007b730);
            [NSThread sleepForTimeInterval:rdx];
            rbx = rbx - 0x1;
    } while (rbx >= 0x2);
    _Block_object_dispose(&var_68, 0x8);
    _Block_object_dispose(&var_38, 0x8);
    rax = *(*(&var_68 + 0x8) + 0x28);
    return rax;
}

/* */

void -[OPersistentDataStoreClient stopService](void * self, void * _cmd) {
    r15 = self;
    var_38 = @"junk";
    var_30 = @"data";
    r14 = [NSDictionary dictionaryWithObjects:rdx forKeys:rcx count:0x1];
    rbx = *ivar_offset(mRemoteProxy);
    if ([*(r15 + rbx) conformsToProtocol:@protocol(OPersistentDataStoreServiceProtocol)] != 0x0) {
            [*(r15 + rbx) stopService:r14 withReply:^ {/* block implemented at ___41-[OPersistentDataStoreClient stopService]_block_invoke */ } }];
    }
    if (*___stack_chk_guard != *___stack_chk_guard) {
            __stack_chk_fail();
    }
    return;
}
```