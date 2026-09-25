# V2R cluster inventory

2026-09-25T14:24:45.682896+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/home`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/tmp`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/var/tmp`: 319155691520 available bytes; 82.20% used; 112476975 free inodes.

server1 `/mnt/raid5`: 364067659776 available bytes; 98.33% used; 337547381 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/home`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/tmp`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/var/tmp`: 4721176576 available bytes; 99.74% used; 110407464 free inodes.

server2 `/mnt/raid5`: 321047486464 available bytes; 97.78% used; 445075462 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.

server3 `/home`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.

server3 `/data`: 142209118208 available bytes; 98.03% used; 225808791 free inodes.

server3 `/tmp`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.

server3 `/var/tmp`: 84272414720 available bytes; 95.30% used; 114154468 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server4 `/home`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server4 `/data`: 231443136512 available bytes; 96.80% used; 224946639 free inodes.

server4 `/tmp`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server4 `/var/tmp`: 105654497280 available bytes; 94.10% used; 114349711 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
