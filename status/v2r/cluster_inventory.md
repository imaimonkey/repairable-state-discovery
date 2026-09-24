# V2R cluster inventory

2026-09-24T00:27:51.166737+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | [] | ['/tmp', '/var/tmp', '/mnt/raid5'] |

server1 `/`: 325550448640 available bytes; 81.84% used; 112500618 free inodes.

server1 `/home`: 325550448640 available bytes; 81.84% used; 112500618 free inodes.

server1 `/tmp`: 325550448640 available bytes; 81.84% used; 112500618 free inodes.

server1 `/var/tmp`: 325550448640 available bytes; 81.84% used; 112500618 free inodes.

server1 `/mnt/raid5`: 1153226723328 available bytes; 94.71% used; 337735162 free inodes.
| server2 | True | [] | [] |

server2 `/`: 40996581376 available bytes; 97.71% used; 110432349 free inodes.

server2 `/home`: 40996581376 available bytes; 97.71% used; 110432349 free inodes.

server2 `/tmp`: 40996581376 available bytes; 97.71% used; 110432349 free inodes.

server2 `/var/tmp`: 40996581376 available bytes; 97.71% used; 110432349 free inodes.

server2 `/mnt/raid5`: 532862439424 available bytes; 96.32% used; 445203375 free inodes.
| server3 | True | [] | ['/tmp', '/var/tmp'] |

server3 `/`: 292236640256 available bytes; 83.69% used; 114186472 free inodes.

server3 `/home`: 292236640256 available bytes; 83.69% used; 114186472 free inodes.

server3 `/data`: 82240184320 available bytes; 98.86% used; 225844262 free inodes.

server3 `/tmp`: 292236640256 available bytes; 83.69% used; 114186472 free inodes.

server3 `/var/tmp`: 292236640256 available bytes; 83.69% used; 114186472 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 106083549184 available bytes; 94.08% used; 114350403 free inodes.

server4 `/home`: 106083549184 available bytes; 94.08% used; 114350403 free inodes.

server4 `/data`: 292921700352 available bytes; 95.95% used; 225414579 free inodes.

server4 `/tmp`: 106083549184 available bytes; 94.08% used; 114350403 free inodes.

server4 `/var/tmp`: 106083549184 available bytes; 94.08% used; 114350403 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
