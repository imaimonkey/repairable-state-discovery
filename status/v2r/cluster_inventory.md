# V2R cluster inventory

2026-09-24T05:01:07.081129+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324614639616 available bytes; 81.89% used; 112492684 free inodes.

server1 `/home`: 324614639616 available bytes; 81.89% used; 112492684 free inodes.

server1 `/tmp`: 324614639616 available bytes; 81.89% used; 112492684 free inodes.

server1 `/var/tmp`: 324614639616 available bytes; 81.89% used; 112492684 free inodes.

server1 `/mnt/raid5`: 484362596352 available bytes; 97.78% used; 337724571 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 40759054336 available bytes; 97.73% used; 110430402 free inodes.

server2 `/home`: 40759054336 available bytes; 97.73% used; 110430402 free inodes.

server2 `/tmp`: 40759054336 available bytes; 97.73% used; 110430402 free inodes.

server2 `/var/tmp`: 40759054336 available bytes; 97.73% used; 110430402 free inodes.

server2 `/mnt/raid5`: 523566514176 available bytes; 96.38% used; 445195052 free inodes.
| server3 | True | ['1'] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 292010254336 available bytes; 83.70% used; 114177268 free inodes.

server3 `/home`: 292010254336 available bytes; 83.70% used; 114177268 free inodes.

server3 `/data`: 23297851392 available bytes; 99.68% used; 225840409 free inodes.

server3 `/tmp`: 292010254336 available bytes; 83.70% used; 114177268 free inodes.

server3 `/var/tmp`: 292010254336 available bytes; 83.70% used; 114177268 free inodes.
| server4 | True | ['7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105826983936 available bytes; 94.09% used; 114349388 free inodes.

server4 `/home`: 105826983936 available bytes; 94.09% used; 114349388 free inodes.

server4 `/data`: 252704874496 available bytes; 96.51% used; 225366802 free inodes.

server4 `/tmp`: 105826983936 available bytes; 94.09% used; 114349388 free inodes.

server4 `/var/tmp`: 105826983936 available bytes; 94.09% used; 114349388 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
