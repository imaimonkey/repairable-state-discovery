# V2R cluster inventory

2026-09-24T02:32:09.554645+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 325383593984 available bytes; 81.85% used; 112498851 free inodes.

server1 `/home`: 325383593984 available bytes; 81.85% used; 112498851 free inodes.

server1 `/tmp`: 325383593984 available bytes; 81.85% used; 112498851 free inodes.

server1 `/var/tmp`: 325383593984 available bytes; 81.85% used; 112498851 free inodes.

server1 `/mnt/raid5`: 638623285248 available bytes; 97.07% used; 337733237 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40890822656 available bytes; 97.72% used; 110431524 free inodes.

server2 `/home`: 40890822656 available bytes; 97.72% used; 110431524 free inodes.

server2 `/tmp`: 40890822656 available bytes; 97.72% used; 110431524 free inodes.

server2 `/var/tmp`: 40890822656 available bytes; 97.72% used; 110431524 free inodes.

server2 `/mnt/raid5`: 528938840064 available bytes; 96.35% used; 445199474 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 291856392192 available bytes; 83.71% used; 114163134 free inodes.

server3 `/home`: 291856392192 available bytes; 83.71% used; 114163134 free inodes.

server3 `/data`: 39754117120 available bytes; 99.45% used; 225846352 free inodes.

server3 `/tmp`: 291856392192 available bytes; 83.71% used; 114163134 free inodes.

server3 `/var/tmp`: 291856392192 available bytes; 83.71% used; 114163134 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106003656704 available bytes; 94.08% used; 114349842 free inodes.

server4 `/home`: 106003656704 available bytes; 94.08% used; 114349842 free inodes.

server4 `/data`: 289734316032 available bytes; 96.00% used; 225387484 free inodes.

server4 `/tmp`: 106003656704 available bytes; 94.08% used; 114349842 free inodes.

server4 `/var/tmp`: 106003656704 available bytes; 94.08% used; 114349842 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
