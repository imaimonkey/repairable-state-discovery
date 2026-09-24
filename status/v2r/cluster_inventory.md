# V2R cluster inventory

2026-09-24T00:12:23.501717+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325572202496 available bytes; 81.84% used; 112500788 free inodes.

server1 `/home`: 325572202496 available bytes; 81.84% used; 112500788 free inodes.

server1 `/tmp`: 325572202496 available bytes; 81.84% used; 112500788 free inodes.

server1 `/var/tmp`: 325572202496 available bytes; 81.84% used; 112500788 free inodes.

server1 `/mnt/raid5`: 1206441254912 available bytes; 94.47% used; 337735262 free inodes.
| server2 | True | [] | [] |

server2 `/`: 41006804992 available bytes; 97.71% used; 110432402 free inodes.

server2 `/home`: 41006804992 available bytes; 97.71% used; 110432402 free inodes.

server2 `/tmp`: 41006804992 available bytes; 97.71% used; 110432402 free inodes.

server2 `/var/tmp`: 41006804992 available bytes; 97.71% used; 110432402 free inodes.

server2 `/mnt/raid5`: 533325008896 available bytes; 96.31% used; 445203701 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292599177216 available bytes; 83.67% used; 114209092 free inodes.

server3 `/home`: 292599177216 available bytes; 83.67% used; 114209092 free inodes.

server3 `/data`: 82255544320 available bytes; 98.86% used; 225844544 free inodes.

server3 `/tmp`: 292599177216 available bytes; 83.67% used; 114209092 free inodes.

server3 `/var/tmp`: 292599177216 available bytes; 83.67% used; 114209092 free inodes.
| server4 | True | ['3', '4', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106111438848 available bytes; 94.08% used; 114350843 free inodes.

server4 `/home`: 106111438848 available bytes; 94.08% used; 114350843 free inodes.

server4 `/data`: 292910944256 available bytes; 95.95% used; 225414568 free inodes.

server4 `/tmp`: 106111438848 available bytes; 94.08% used; 114350843 free inodes.

server4 `/var/tmp`: 106111438848 available bytes; 94.08% used; 114350843 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
