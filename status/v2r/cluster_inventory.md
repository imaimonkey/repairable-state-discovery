# V2R cluster inventory

2026-09-24T17:36:51.163233+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324004134912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/home`: 324004134912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/tmp`: 324004134912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/var/tmp`: 324004134912 available bytes; 81.92% used; 112481448 free inodes.

server1 `/mnt/raid5`: 416441577472 available bytes; 98.09% used; 337645595 free inodes.
| server2 | True | ['7'] | [] | reference_compatible=False |

server2 `/`: 56914026496 available bytes; 96.82% used; 110412457 free inodes.

server2 `/home`: 56914026496 available bytes; 96.82% used; 110412457 free inodes.

server2 `/tmp`: 56914026496 available bytes; 96.82% used; 110412457 free inodes.

server2 `/var/tmp`: 56914026496 available bytes; 96.82% used; 110412457 free inodes.

server2 `/mnt/raid5`: 498592813056 available bytes; 96.55% used; 445162287 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84407267328 available bytes; 95.29% used; 114156150 free inodes.

server3 `/home`: 84407267328 available bytes; 95.29% used; 114156150 free inodes.

server3 `/data`: 158888271872 available bytes; 97.80% used; 225786721 free inodes.

server3 `/tmp`: 84407267328 available bytes; 95.29% used; 114156150 free inodes.

server3 `/var/tmp`: 84407267328 available bytes; 95.29% used; 114156150 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105672835072 available bytes; 94.10% used; 114348559 free inodes.

server4 `/home`: 105672835072 available bytes; 94.10% used; 114348559 free inodes.

server4 `/data`: 89066303488 available bytes; 98.77% used; 225253873 free inodes.

server4 `/tmp`: 105672835072 available bytes; 94.10% used; 114348559 free inodes.

server4 `/var/tmp`: 105672835072 available bytes; 94.10% used; 114348559 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
