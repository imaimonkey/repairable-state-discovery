# V2R cluster inventory

2026-09-25T21:29:38.448722+00:00

Read-only observation; idle candidates still require Slurm allocation, safe immutable execution worktree, exact reference replay compatibility, and measured shard storage gate.

| Server | Observed | Idle GPU candidates | Writable safe filesystem candidates | Reference-compatible |
|---|---|---|---|---|
| server1 | True | ['4', '6', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server1 `/`: 318701670400 available bytes; 82.22% used; 112476322 free inodes.

server1 `/home`: 318701670400 available bytes; 82.22% used; 112476322 free inodes.

server1 `/tmp`: 318701670400 available bytes; 82.22% used; 112476322 free inodes.

server1 `/var/tmp`: 318701670400 available bytes; 82.22% used; 112476322 free inodes.

server1 `/mnt/raid5`: 346761453568 available bytes; 98.41% used; 337539292 free inodes.
| server2 | True | ['6'] | [] | reference_compatible=False |

server2 `/`: 22905237504 available bytes; 98.72% used; 110405682 free inodes.

server2 `/home`: 22905237504 available bytes; 98.72% used; 110405682 free inodes.

server2 `/tmp`: 22905237504 available bytes; 98.72% used; 110405682 free inodes.

server2 `/var/tmp`: 22905237504 available bytes; 98.72% used; 110405682 free inodes.

server2 `/mnt/raid5`: 301291302912 available bytes; 97.92% used; 445055026 free inodes.
| server3 | True | [] | [] | reference_compatible=True |

server3 `/`: 84363112448 available bytes; 95.29% used; 114152618 free inodes.

server3 `/home`: 84363112448 available bytes; 95.29% used; 114152618 free inodes.

server3 `/data`: 125898543104 available bytes; 98.26% used; 225807010 free inodes.

server3 `/tmp`: 84363112448 available bytes; 95.29% used; 114152618 free inodes.

server3 `/var/tmp`: 84363112448 available bytes; 95.29% used; 114152618 free inodes.
| server4 | True | ['3', '7'] | ['/tmp', '/var/tmp'] | reference_compatible=False |

server4 `/`: 105389064192 available bytes; 94.12% used; 114347331 free inodes.

server4 `/home`: 105389064192 available bytes; 94.12% used; 114347331 free inodes.

server4 `/data`: 217451864064 available bytes; 96.99% used; 224920126 free inodes.

server4 `/tmp`: 105389064192 available bytes; 94.12% used; 114347331 free inodes.

server4 `/var/tmp`: 105389064192 available bytes; 94.12% used; 114347331 free inodes.

server1 SSH access failure leaves GPU process/disk/worktree details unobserved. Its Slurm allocations are observed; it is not eligible. Existing jobs and monitor are never cancelled by this tool.
