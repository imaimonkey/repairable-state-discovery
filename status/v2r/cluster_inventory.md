# V2R cluster inventory

2026-09-24T21:33:04.398232+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['3'] | ['/tmp', '/var/tmp'] |

server1 `/`: 323954085888 available bytes; 81.93% used; 112481420 free inodes.

server1 `/home`: 323954085888 available bytes; 81.93% used; 112481420 free inodes.

server1 `/tmp`: 323954085888 available bytes; 81.93% used; 112481420 free inodes.

server1 `/var/tmp`: 323954085888 available bytes; 81.93% used; 112481420 free inodes.

server1 `/mnt/raid5`: 415493578752 available bytes; 98.09% used; 337627112 free inodes.
| server2 | True | [] | [] |

server2 `/`: 30139637760 available bytes; 98.32% used; 110411342 free inodes.

server2 `/home`: 30139637760 available bytes; 98.32% used; 110411342 free inodes.

server2 `/tmp`: 30139637760 available bytes; 98.32% used; 110411342 free inodes.

server2 `/var/tmp`: 30139637760 available bytes; 98.32% used; 110411342 free inodes.

server2 `/mnt/raid5`: 490321211392 available bytes; 96.61% used; 445155270 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84387201024 available bytes; 95.29% used; 114156095 free inodes.

server3 `/home`: 84387201024 available bytes; 95.29% used; 114156095 free inodes.

server3 `/data`: 150248579072 available bytes; 97.92% used; 225803142 free inodes.

server3 `/tmp`: 84387201024 available bytes; 95.29% used; 114156095 free inodes.

server3 `/var/tmp`: 84387201024 available bytes; 95.29% used; 114156095 free inodes.
| server4 | True | ['1', '4', '5'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105630105600 available bytes; 94.11% used; 114348350 free inodes.

server4 `/home`: 105630105600 available bytes; 94.11% used; 114348350 free inodes.

server4 `/data`: 82911694848 available bytes; 98.85% used; 225252573 free inodes.

server4 `/tmp`: 105630105600 available bytes; 94.11% used; 114348350 free inodes.

server4 `/var/tmp`: 105630105600 available bytes; 94.11% used; 114348350 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
