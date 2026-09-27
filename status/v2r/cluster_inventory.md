# V2R cluster inventory

2026-09-27T14:59:16.906015+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates |
|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] |

server1 `/`: 304747360256 available bytes; 83.00% used; 112401390 free inodes.

server1 `/home`: 304747360256 available bytes; 83.00% used; 112401390 free inodes.

server1 `/tmp`: 304747360256 available bytes; 83.00% used; 112401390 free inodes.

server1 `/var/tmp`: 304747360256 available bytes; 83.00% used; 112401390 free inodes.

server1 `/mnt/raid5`: 630115614720 available bytes; 97.11% used; 337424040 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] |

server2 `/`: 13413072896 available bytes; 99.25% used; 110351801 free inodes.

server2 `/home`: 13413072896 available bytes; 99.25% used; 110351801 free inodes.

server2 `/tmp`: 13413072896 available bytes; 99.25% used; 110351801 free inodes.

server2 `/var/tmp`: 13413072896 available bytes; 99.25% used; 110351801 free inodes.

server2 `/mnt/raid5`: 525204819968 available bytes; 96.37% used; 444721515 free inodes.
| server3 | True | ['0', '1'] | [] |

server3 `/`: 78558863360 available bytes; 95.62% used; 114062773 free inodes.

server3 `/home`: 78558863360 available bytes; 95.62% used; 114062773 free inodes.

server3 `/data`: 1328688783360 available bytes; 81.64% used; 225756495 free inodes.

server3 `/tmp`: 78558863360 available bytes; 95.62% used; 114062773 free inodes.

server3 `/var/tmp`: 78558863360 available bytes; 95.62% used; 114062773 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] |

server4 `/`: 109349064704 available bytes; 93.90% used; 114372743 free inodes.

server4 `/home`: 109349064704 available bytes; 93.90% used; 114372743 free inodes.

server4 `/data`: 350411309056 available bytes; 95.16% used; 224727235 free inodes.

server4 `/tmp`: 109349064704 available bytes; 93.90% used; 114372743 free inodes.

server4 `/var/tmp`: 109349064704 available bytes; 93.90% used; 114372743 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
