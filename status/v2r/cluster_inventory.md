# V2R cluster inventory

2026-09-25T14:35:21.694279+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319157473280 available bytes; 82.20% used; 112476978 free inodes.

server1 `/home`: 319157473280 available bytes; 82.20% used; 112476978 free inodes.

server1 `/tmp`: 319157473280 available bytes; 82.20% used; 112476978 free inodes.

server1 `/var/tmp`: 319157473280 available bytes; 82.20% used; 112476978 free inodes.

server1 `/mnt/raid5`: 364126748672 available bytes; 98.33% used; 337546820 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 12799700992 available bytes; 99.29% used; 110407875 free inodes.

server2 `/home`: 12799700992 available bytes; 99.29% used; 110407875 free inodes.

server2 `/tmp`: 12799700992 available bytes; 99.29% used; 110407875 free inodes.

server2 `/var/tmp`: 12799700992 available bytes; 99.29% used; 110407875 free inodes.

server2 `/mnt/raid5`: 320805212160 available bytes; 97.78% used; 445074986 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84263841792 available bytes; 95.30% used; 114154468 free inodes.

server3 `/home`: 84263841792 available bytes; 95.30% used; 114154468 free inodes.

server3 `/data`: 142207381504 available bytes; 98.03% used; 225808614 free inodes.

server3 `/tmp`: 84263841792 available bytes; 95.30% used; 114154468 free inodes.

server3 `/var/tmp`: 84263841792 available bytes; 95.30% used; 114154468 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105654185984 available bytes; 94.10% used; 114349709 free inodes.

server4 `/home`: 105654185984 available bytes; 94.10% used; 114349709 free inodes.

server4 `/data`: 231433670656 available bytes; 96.80% used; 224946162 free inodes.

server4 `/tmp`: 105654185984 available bytes; 94.10% used; 114349709 free inodes.

server4 `/var/tmp`: 105654185984 available bytes; 94.10% used; 114349709 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
