# V2R cluster inventory

2026-09-24T11:57:24.695247+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324287823872 available bytes; 81.91% used; 112488398 free inodes.

server1 `/home`: 324287823872 available bytes; 81.91% used; 112488398 free inodes.

server1 `/tmp`: 324287823872 available bytes; 81.91% used; 112488398 free inodes.

server1 `/var/tmp`: 324287823872 available bytes; 81.91% used; 112488398 free inodes.

server1 `/mnt/raid5`: 382646779904 available bytes; 98.24% used; 337685979 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57632632832 available bytes; 96.78% used; 110429726 free inodes.

server2 `/home`: 57632632832 available bytes; 96.78% used; 110429726 free inodes.

server2 `/tmp`: 57632632832 available bytes; 96.78% used; 110429726 free inodes.

server2 `/var/tmp`: 57632632832 available bytes; 96.78% used; 110429726 free inodes.

server2 `/mnt/raid5`: 509826473984 available bytes; 96.48% used; 445173142 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85750833152 available bytes; 95.21% used; 114198336 free inodes.

server3 `/home`: 85750833152 available bytes; 95.21% used; 114198336 free inodes.

server3 `/data`: 163609022464 available bytes; 97.74% used; 225815736 free inodes.

server3 `/tmp`: 85750833152 available bytes; 95.21% used; 114198336 free inodes.

server3 `/var/tmp`: 85750833152 available bytes; 95.21% used; 114198336 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105727238144 available bytes; 94.10% used; 114348830 free inodes.

server4 `/home`: 105727238144 available bytes; 94.10% used; 114348830 free inodes.

server4 `/data`: 115362787328 available bytes; 98.41% used; 225257844 free inodes.

server4 `/tmp`: 105727238144 available bytes; 94.10% used; 114348830 free inodes.

server4 `/var/tmp`: 105727238144 available bytes; 94.10% used; 114348830 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
