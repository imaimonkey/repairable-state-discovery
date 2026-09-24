# V2R cluster inventory

2026-09-24T00:38:40.661914+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325543350272 available bytes; 81.84% used; 112500495 free inodes.

server1 `/home`: 325543350272 available bytes; 81.84% used; 112500495 free inodes.

server1 `/tmp`: 325543350272 available bytes; 81.84% used; 112500495 free inodes.

server1 `/var/tmp`: 325543350272 available bytes; 81.84% used; 112500495 free inodes.

server1 `/mnt/raid5`: 1108058148864 available bytes; 94.92% used; 337735049 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40986996736 available bytes; 97.71% used; 110432308 free inodes.

server2 `/home`: 40986996736 available bytes; 97.71% used; 110432308 free inodes.

server2 `/tmp`: 40986996736 available bytes; 97.71% used; 110432308 free inodes.

server2 `/var/tmp`: 40986996736 available bytes; 97.71% used; 110432308 free inodes.

server2 `/mnt/raid5`: 532509728768 available bytes; 96.32% used; 445203062 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292288282624 available bytes; 83.69% used; 114187335 free inodes.

server3 `/home`: 292288282624 available bytes; 83.69% used; 114187335 free inodes.

server3 `/data`: 82234626048 available bytes; 98.86% used; 225844065 free inodes.

server3 `/tmp`: 292288282624 available bytes; 83.69% used; 114187335 free inodes.

server3 `/var/tmp`: 292288282624 available bytes; 83.69% used; 114187335 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106065387520 available bytes; 94.08% used; 114350118 free inodes.

server4 `/home`: 106065387520 available bytes; 94.08% used; 114350118 free inodes.

server4 `/data`: 292919070720 available bytes; 95.95% used; 225414580 free inodes.

server4 `/tmp`: 106065387520 available bytes; 94.08% used; 114350118 free inodes.

server4 `/var/tmp`: 106065387520 available bytes; 94.08% used; 114350118 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
