# V2R cluster inventory

2026-09-25T14:24:39.377658+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] |

server1 `/`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/home`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/tmp`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/var/tmp`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/mnt/raid5`: 364067766272 available bytes; 98.33% used; 337547381 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] |

server2 `/`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/home`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/tmp`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/var/tmp`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/mnt/raid5`: 321051475968 available bytes; 97.78% used; 445075466 free inodes.
| server3 | True | [] | [] |

server3 `/`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.

server3 `/home`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.

server3 `/data`: 142209282048 available bytes; 98.03% used; 225808806 free inodes.

server3 `/tmp`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.

server3 `/var/tmp`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] |

server4 `/`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server4 `/home`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server4 `/data`: 231443681280 available bytes; 96.80% used; 224946647 free inodes.

server4 `/tmp`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server4 `/var/tmp`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
