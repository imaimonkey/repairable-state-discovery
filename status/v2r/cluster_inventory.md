# V2R cluster inventory

2026-09-25T15:01:30.304460+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 319136178176 available bytes; 82.20% used; 112476955 free inodes.

server1 `/home`: 319136178176 available bytes; 82.20% used; 112476955 free inodes.

server1 `/tmp`: 319136178176 available bytes; 82.20% used; 112476955 free inodes.

server1 `/var/tmp`: 319136178176 available bytes; 82.20% used; 112476955 free inodes.

server1 `/mnt/raid5`: 364015710208 available bytes; 98.33% used; 337546279 free inodes.
| server2 | True | ['3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 14377439232 available bytes; 99.20% used; 110407649 free inodes.

server2 `/home`: 14377439232 available bytes; 99.20% used; 110407649 free inodes.

server2 `/tmp`: 14377439232 available bytes; 99.20% used; 110407649 free inodes.

server2 `/var/tmp`: 14377439232 available bytes; 99.20% used; 110407649 free inodes.

server2 `/mnt/raid5`: 320244809728 available bytes; 97.79% used; 445073978 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84427264000 available bytes; 95.29% used; 114153446 free inodes.

server3 `/home`: 84427264000 available bytes; 95.29% used; 114153446 free inodes.

server3 `/data`: 142192549888 available bytes; 98.03% used; 225808176 free inodes.

server3 `/tmp`: 84427264000 available bytes; 95.29% used; 114153446 free inodes.

server3 `/var/tmp`: 84427264000 available bytes; 95.29% used; 114153446 free inodes.
| server4 | True | ['2', '3'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105636655104 available bytes; 94.11% used; 114349708 free inodes.

server4 `/home`: 105636655104 available bytes; 94.11% used; 114349708 free inodes.

server4 `/data`: 231414292480 available bytes; 96.80% used; 224945016 free inodes.

server4 `/tmp`: 105636655104 available bytes; 94.11% used; 114349708 free inodes.

server4 `/var/tmp`: 105636655104 available bytes; 94.11% used; 114349708 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
