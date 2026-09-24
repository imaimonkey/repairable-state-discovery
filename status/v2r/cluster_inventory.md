# V2R cluster inventory

2026-09-24T06:11:48.840591+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324522000384 available bytes; 81.90% used; 112491828 free inodes.

server1 `/home`: 324522000384 available bytes; 81.90% used; 112491828 free inodes.

server1 `/tmp`: 324522000384 available bytes; 81.90% used; 112491828 free inodes.

server1 `/var/tmp`: 324522000384 available bytes; 81.90% used; 112491828 free inodes.

server1 `/mnt/raid5`: 517600952320 available bytes; 97.63% used; 337723792 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57894899712 available bytes; 96.77% used; 110431266 free inodes.

server2 `/home`: 57894899712 available bytes; 96.77% used; 110431266 free inodes.

server2 `/tmp`: 57894899712 available bytes; 96.77% used; 110431266 free inodes.

server2 `/var/tmp`: 57894899712 available bytes; 96.77% used; 110431266 free inodes.

server2 `/mnt/raid5`: 520806744064 available bytes; 96.40% used; 445192588 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126813306880 available bytes; 92.92% used; 114175977 free inodes.

server3 `/home`: 126813306880 available bytes; 92.92% used; 114175977 free inodes.

server3 `/data`: 161311604736 available bytes; 97.77% used; 225836107 free inodes.

server3 `/tmp`: 126813306880 available bytes; 92.92% used; 114175977 free inodes.

server3 `/var/tmp`: 126813306880 available bytes; 92.92% used; 114175977 free inodes.
| server4 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105806508032 available bytes; 94.10% used; 114349319 free inodes.

server4 `/home`: 105806508032 available bytes; 94.10% used; 114349319 free inodes.

server4 `/data`: 339772018688 available bytes; 95.30% used; 225374060 free inodes.

server4 `/tmp`: 105806508032 available bytes; 94.10% used; 114349319 free inodes.

server4 `/var/tmp`: 105806508032 available bytes; 94.10% used; 114349319 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
