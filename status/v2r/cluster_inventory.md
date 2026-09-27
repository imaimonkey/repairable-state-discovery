# V2R cluster inventory

2026-09-27T14:51:39.274249+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304748310528 available bytes; 83.00% used; 112401409 free inodes.

server1 `/home`: 304748310528 available bytes; 83.00% used; 112401409 free inodes.

server1 `/tmp`: 304748310528 available bytes; 83.00% used; 112401409 free inodes.

server1 `/var/tmp`: 304748310528 available bytes; 83.00% used; 112401409 free inodes.

server1 `/mnt/raid5`: 630115287040 available bytes; 97.11% used; 337424041 free inodes.
| server2 | True | ['2', '3', '4', '5', '6'] | [] | reference_compatible=False |

server2 `/`: 13413453824 available bytes; 99.25% used; 110351801 free inodes.

server2 `/home`: 13413453824 available bytes; 99.25% used; 110351801 free inodes.

server2 `/tmp`: 13413453824 available bytes; 99.25% used; 110351801 free inodes.

server2 `/var/tmp`: 13413453824 available bytes; 99.25% used; 110351801 free inodes.

server2 `/mnt/raid5`: 525819662336 available bytes; 96.37% used; 444721724 free inodes.
| server3 | True | ['0', '1'] | [] | reference_compatible=True |

server3 `/`: 78558728192 available bytes; 95.62% used; 114062775 free inodes.

server3 `/home`: 78558728192 available bytes; 95.62% used; 114062775 free inodes.

server3 `/data`: 1328698843136 available bytes; 81.64% used; 225756638 free inodes.

server3 `/tmp`: 78558728192 available bytes; 95.62% used; 114062775 free inodes.

server3 `/var/tmp`: 78558728192 available bytes; 95.62% used; 114062775 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109357592576 available bytes; 93.90% used; 114372744 free inodes.

server4 `/home`: 109357592576 available bytes; 93.90% used; 114372744 free inodes.

server4 `/data`: 350420996096 available bytes; 95.16% used; 224727292 free inodes.

server4 `/tmp`: 109357592576 available bytes; 93.90% used; 114372744 free inodes.

server4 `/var/tmp`: 109357592576 available bytes; 93.90% used; 114372744 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
