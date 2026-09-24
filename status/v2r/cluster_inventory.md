# V2R cluster inventory

2026-09-24T11:32:19.791021+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 324347568128 available bytes; 81.91% used; 112488847 free inodes.

server1 `/home`: 324347568128 available bytes; 81.91% used; 112488847 free inodes.

server1 `/tmp`: 324347568128 available bytes; 81.91% used; 112488847 free inodes.

server1 `/var/tmp`: 324347568128 available bytes; 81.91% used; 112488847 free inodes.

server1 `/mnt/raid5`: 442952839168 available bytes; 97.97% used; 337689216 free inodes.
| server2 | True | ['7'] | [] |

server2 `/`: 57661689856 available bytes; 96.78% used; 110429978 free inodes.

server2 `/home`: 57661689856 available bytes; 96.78% used; 110429978 free inodes.

server2 `/tmp`: 57661689856 available bytes; 96.78% used; 110429978 free inodes.

server2 `/var/tmp`: 57661689856 available bytes; 96.78% used; 110429978 free inodes.

server2 `/mnt/raid5`: 510564900864 available bytes; 96.47% used; 445173322 free inodes.
| server3 | True | [] | [] |

server3 `/`: 85736681472 available bytes; 95.22% used; 114195934 free inodes.

server3 `/home`: 85736681472 available bytes; 95.22% used; 114195934 free inodes.

server3 `/data`: 163787784192 available bytes; 97.74% used; 225816607 free inodes.

server3 `/tmp`: 85736681472 available bytes; 95.22% used; 114195934 free inodes.

server3 `/var/tmp`: 85736681472 available bytes; 95.22% used; 114195934 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] |

server4 `/`: 105730846720 available bytes; 94.10% used; 114348877 free inodes.

server4 `/home`: 105730846720 available bytes; 94.10% used; 114348877 free inodes.

server4 `/data`: 115638218752 available bytes; 98.40% used; 225258066 free inodes.

server4 `/tmp`: 105730846720 available bytes; 94.10% used; 114348877 free inodes.

server4 `/var/tmp`: 105730846720 available bytes; 94.10% used; 114348877 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
