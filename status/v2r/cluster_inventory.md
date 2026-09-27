# V2R cluster inventory

2026-09-27T14:45:32.353138+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['1', '5', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 304749789184 available bytes; 83.00% used; 112401411 free inodes.

server1 `/home`: 304749789184 available bytes; 83.00% used; 112401411 free inodes.

server1 `/tmp`: 304749789184 available bytes; 83.00% used; 112401411 free inodes.

server1 `/var/tmp`: 304749789184 available bytes; 83.00% used; 112401411 free inodes.

server1 `/mnt/raid5`: 630116016128 available bytes; 97.11% used; 337424044 free inodes.
| server2 | True | ['2'] | [] | reference_compatible=False |

server2 `/`: 13404434432 available bytes; 99.25% used; 110351796 free inodes.

server2 `/home`: 13404434432 available bytes; 99.25% used; 110351796 free inodes.

server2 `/tmp`: 13404434432 available bytes; 99.25% used; 110351796 free inodes.

server2 `/var/tmp`: 13404434432 available bytes; 99.25% used; 110351796 free inodes.

server2 `/mnt/raid5`: 525968089088 available bytes; 96.37% used; 444722165 free inodes.
| server3 | True | ['0', '1'] | [] | reference_compatible=True |

server3 `/`: 78558044160 available bytes; 95.62% used; 114062777 free inodes.

server3 `/home`: 78558044160 available bytes; 95.62% used; 114062777 free inodes.

server3 `/data`: 1328701218816 available bytes; 81.64% used; 225756695 free inodes.

server3 `/tmp`: 78558044160 available bytes; 95.62% used; 114062777 free inodes.

server3 `/var/tmp`: 78558044160 available bytes; 95.62% used; 114062777 free inodes.
| server4 | True | ['1', '3', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 109761662976 available bytes; 93.87% used; 114372745 free inodes.

server4 `/home`: 109761662976 available bytes; 93.87% used; 114372745 free inodes.

server4 `/data`: 350434349056 available bytes; 95.16% used; 224727324 free inodes.

server4 `/tmp`: 109761662976 available bytes; 93.87% used; 114372745 free inodes.

server4 `/var/tmp`: 109761662976 available bytes; 93.87% used; 114372745 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
