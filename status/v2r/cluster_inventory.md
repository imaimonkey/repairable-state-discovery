# V2R cluster inventory

2026-09-24T06:47:31.286292+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['5', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 324485922816 available bytes; 81.90% used; 112491492 free inodes.

server1 `/home`: 324485922816 available bytes; 81.90% used; 112491492 free inodes.

server1 `/tmp`: 324485922816 available bytes; 81.90% used; 112491492 free inodes.

server1 `/var/tmp`: 324485922816 available bytes; 81.90% used; 112491492 free inodes.

server1 `/mnt/raid5`: 517430718464 available bytes; 97.63% used; 337722873 free inodes.
| server2 | True | [] | [] | reference_compatible=False |

server2 `/`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/home`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/tmp`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/var/tmp`: 57873580032 available bytes; 96.77% used; 110431203 free inodes.

server2 `/mnt/raid5`: 519709552640 available bytes; 96.41% used; 445191495 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=True |

server3 `/`: 126712373248 available bytes; 92.93% used; 114172600 free inodes.

server3 `/home`: 126712373248 available bytes; 92.93% used; 114172600 free inodes.

server3 `/data`: 139319554048 available bytes; 98.07% used; 225835000 free inodes.

server3 `/tmp`: 126712373248 available bytes; 92.93% used; 114172600 free inodes.

server3 `/var/tmp`: 126712373248 available bytes; 92.93% used; 114172600 free inodes.
| server4 | True | [] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105804562432 available bytes; 94.10% used; 114349238 free inodes.

server4 `/home`: 105804562432 available bytes; 94.10% used; 114349238 free inodes.

server4 `/data`: 313648259072 available bytes; 95.67% used; 225368402 free inodes.

server4 `/tmp`: 105804562432 available bytes; 94.10% used; 114349238 free inodes.

server4 `/var/tmp`: 105804562432 available bytes; 94.10% used; 114349238 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
