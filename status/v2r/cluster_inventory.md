# V2R cluster inventory

2026-09-26T07:34:09.834730+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '4', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318767632384 available bytes; 82.22% used; 112476289 free inodes.

server1 `/home`: 318767632384 available bytes; 82.22% used; 112476289 free inodes.

server1 `/tmp`: 318767632384 available bytes; 82.22% used; 112476289 free inodes.

server1 `/var/tmp`: 318767632384 available bytes; 82.22% used; 112476289 free inodes.

server1 `/mnt/raid5`: 219233726464 available bytes; 98.99% used; 337539233 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/home`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/tmp`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/var/tmp`: 22318522368 available bytes; 98.75% used; 110403927 free inodes.

server2 `/mnt/raid5`: 271342379008 available bytes; 98.13% used; 445026650 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 82681135104 available bytes; 95.39% used; 114110899 free inodes.

server3 `/home`: 82681135104 available bytes; 95.39% used; 114110899 free inodes.

server3 `/data`: 123980341248 available bytes; 98.29% used; 225821013 free inodes.

server3 `/tmp`: 82681135104 available bytes; 95.39% used; 114110899 free inodes.

server3 `/var/tmp`: 82681135104 available bytes; 95.39% used; 114110899 free inodes.
| server4 | True | ['2', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 106074378240 available bytes; 94.08% used; 114348173 free inodes.

server4 `/home`: 106074378240 available bytes; 94.08% used; 114348173 free inodes.

server4 `/data`: 105867137024 available bytes; 98.54% used; 224922704 free inodes.

server4 `/tmp`: 106074378240 available bytes; 94.08% used; 114348173 free inodes.

server4 `/var/tmp`: 106074378240 available bytes; 94.08% used; 114348173 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
