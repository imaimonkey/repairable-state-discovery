# V2R cluster inventory

2026-09-25T22:17:19.393255+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 318694191104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/home`: 318694191104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/tmp`: 318694191104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/var/tmp`: 318694191104 available bytes; 82.22% used; 112476304 free inodes.

server1 `/mnt/raid5`: 360266788864 available bytes; 98.35% used; 337539002 free inodes.
| server2 | True | ['2'] | [] |

server2 `/`: 22946938880 available bytes; 98.72% used; 110406236 free inodes.

server2 `/home`: 22946938880 available bytes; 98.72% used; 110406236 free inodes.

server2 `/tmp`: 22946938880 available bytes; 98.72% used; 110406236 free inodes.

server2 `/var/tmp`: 22946938880 available bytes; 98.72% used; 110406236 free inodes.

server2 `/mnt/raid5`: 299344494592 available bytes; 97.93% used; 445053427 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84357189632 available bytes; 95.29% used; 114152634 free inodes.

server3 `/home`: 84357189632 available bytes; 95.29% used; 114152634 free inodes.

server3 `/data`: 125870923776 available bytes; 98.26% used; 225806189 free inodes.

server3 `/tmp`: 84357189632 available bytes; 95.29% used; 114152634 free inodes.

server3 `/var/tmp`: 84357189632 available bytes; 95.29% used; 114152634 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105312034816 available bytes; 94.12% used; 114347143 free inodes.

server4 `/home`: 105312034816 available bytes; 94.12% used; 114347143 free inodes.

server4 `/data`: 206942748672 available bytes; 97.14% used; 224917925 free inodes.

server4 `/tmp`: 105312034816 available bytes; 94.12% used; 114347143 free inodes.

server4 `/var/tmp`: 105312034816 available bytes; 94.12% used; 114347143 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
